from typing import Annotated
from fastapi import APIRouter, Form, UploadFile, File, Response
from google.genai import Client
from google.genai.types import Blob, Content,GenerateContentConfig, Part
from PIL import Image
from constants import image_prompt_text
import io
import aiohttp
from dotenv import load_dotenv

load_dotenv()

ai = Client()

router = APIRouter()

@router.post("/generateImage")
async def generate_image(productImages: Annotated[list[str], Form()], 
                         userImage: Annotated[UploadFile, File()]):
    try:
        user_image_content = await userImage.read()
        user_image = Image.open(io.BytesIO(user_image_content))
        current_image_base64 = user_image_content
        current_image_mime_type = Image.MIME.get(user_image.format or "image/png")
        for product_image_url in productImages:
            async with aiohttp.ClientSession() as session:
                async with session.get(product_image_url) as resp:
                    product_image_content = await resp.read()
                    product_image_mime_type = resp.headers.get("Content-Type", "image/png")

            product_part = Part(
                inline_data=Blob(
                    data=product_image_content,
                    mime_type=product_image_mime_type,
                )
            ) 
            person_part = Part(
                inline_data=Blob(
                    data=current_image_base64,
                    mime_type=current_image_mime_type,
                )
            )
            text_part = Part(
                text_data=image_prompt_text.format("Ribbon Joy Pullover")
            )     
            response = ai.models.generate_content(
                model="gemini-2.5-flash_image",
                contents=Content(parts=[person_part, product_part, text_part]),
                config=GenerateContentConfig(response_modalities=["IMAGE"]),
            )
            if response.candidates and len(response.candidates) > 0:
                generated_image = response.candidates[0]
                if(generated_image.content and generated_image.content.parts):
                    for part in generated_image.content.parts:
                        if part.inline_data:
                            current_image_base64 = part.inline_data.data
                            current_image_mime_type = part.inline_data.mime_type

            
        return Response(content=current_image_base64, media_type=current_image_mime_type)
    except Exception as e:
        return {"error": str(e)}