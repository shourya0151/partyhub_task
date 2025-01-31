import replicate
from PIL import Image
from dotenv import load_dotenv
import base64
from io import BytesIO

load_dotenv()

def image_to_data_uri(image_path):
    img = Image.open(image_path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/png;base64,{img_str}"


input = {
    "mask": image_to_data_uri("mask6.png"),
    "image": image_to_data_uri("input_image.png"),
    "prompt": "Create a magical, girly-themed birthday background for a 4-year-old girl, featuring a dreamy pastel wonderland in soft pink, lavender, and pink hues. The scene should blend enchanting elements of unicorns and Barbie, creating a whimsical fairy-tale atmosphere.In the background, include fluffy pink clouds, twinkling stars, and a glowing rainbow arching across the sky. Graceful unicorns with flowing rainbow-colored manes and glittering horns should prance across a field of softly glowing grass, while some with shimmering wings add an ethereal touch. A charming Barbie princess, dressed in a sparkling gown, can stand gracefully among the scene, adding to the fairy-tale magic.Decorate the space with beautifully arranged balloons in various pastel shades, spread evenly throughout the scene rather than clustered in one place. Floating balloon garlands, delicate fairy lights, and tiny fluttering butterflies should enhance the dreamy effect. Elegant drapes, sparkling tiaras, and magical wands can be subtly incorporated to amplify the princess-like feel.The lighting should be soft and glowing, creating a warm and cheerful ambiance. The composition should be well-balanced, leaving ample space in the center for a birthday banner or a table setup. The background should seamlessly blend into the surroundings, making it perfect for a festive and visually stunning celebration.",
    "guidance": 4.9,
    "steps": 45,
    "seed": 642694973038728
   
}

print("Generating base image with Flux Fill Pro...")
fill_output = replicate.run(
    "black-forest-labs/flux-fill-pro",
    input=input
)
with open("1_flux_fill_output.png", "wb") as file:
    file.write(fill_output.read())


# Ultra refinement with Magic Image Refiner
print("Final refinement with Magic Image Refiner...")
refined_output = replicate.run(
    "batouresearch/magic-image-refiner:507ddf6f977a7e30e46c0daefd30de7d563c72322f9e4cf7cbac52ef0f667b13",
    input={
        "image": image_to_data_uri("1_flux_fill_output.png"),
        "prompt": "UHD 4k vogue, birthday theme background balloon and fairy lights.",
        "resemblance": 0.95,
        "creativity": 0.98,
        "enhance_details": True,
        ##"seed": 67874848484,
        "seed": 689744841487284,
        "negative_prompt": "lowres, blurry, pixelated, text, watermark, signature, cropped, bad anatomy, poorly drawn face or hands, extra limbs or fingers, unnatural lighting or colors, cartoonish features, poster-like visuals or frames"
    }
)

for index, item in enumerate(refined_output):
    with open(f"4_magic_refined.png", "wb") as file:
        file.write(item.read())



#Create a magical, girly-themed birthday background for a 4-year-old girl, featuring a dreamy pastel wonderland in soft pink, lavender, and pink hues. The scene should blend enchanting elements of unicorns and Barbie, creating a whimsical fairy-tale atmosphere.In the background, include fluffy pink clouds, twinkling stars, and a glowing rainbow arching across the sky. Graceful unicorns with flowing rainbow-colored manes and glittering horns should prance across a field of softly glowing grass, while some with shimmering wings add an ethereal touch. A charming Barbie princess, dressed in a sparkling gown, can stand gracefully among the scene, adding to the fairy-tale magic.Decorate the space with beautifully arranged balloons in various pastel shades, spread evenly throughout the scene rather than clustered in one place. Floating balloon garlands, delicate fairy lights, and tiny fluttering butterflies should enhance the dreamy effect. Elegant drapes, sparkling tiaras, and magical wands can be subtly incorporated to amplify the princess-like feel.The lighting should be soft and glowing, creating a warm and cheerful ambiance. The composition should be well-balanced, leaving ample space in the center for a birthday banner or a table setup. The background should seamlessly blend into the surroundings, making it perfect for a festive and visually stunning celebration.