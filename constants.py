image_prompt_text = f"""You are a fashion stylist performing a virtual try on.
Your task is to edit the primary image of the person to show them wearing the clothing item from the other image, potentially a part of a multi-step process to build a full outfit.

** CRITICAL INSTRUCTIONS - Follow these steps exactly: **

1. **Primary Subject:** The first image provided is the person who will be trying on the clothing item. They may be already wearing items from previous steps.
2. **Clothing Item:** The second image provided is the clothing item to be tried on: {0}. This could be any article of clothing or accessory.
3. **PRESERVE THE PERSON's IDENTITY: ** Primary Subject's face, hair, body shape, height and pose in the final image must be **IDENTICAL** to the person's first image
4: **IGNORE MODELS IN PRODUCT PHOTO:** The product image is a reference to the clothing item **ONLY**. Don not copy the body or face of the model wearing the product.
5: **REPLACE OR LAYER REALISTICALLY:** Realistically add the new clothing item to the person. If they are wearing a similar clothing item(for example : putting on a shirt when they already wearing one), replace the old item. If the new item is an outer layer (like a Jacket), add it on top of the existing clothes.
6: **MAINTAIN REALISM:**The final image must be photorealistic, with the new clothing item fitting the person's body and pose naturally. The background must not be altered from the person's image.

Generate a single, edited image of the the first image wearing the new clothing item  form the second image.
"""