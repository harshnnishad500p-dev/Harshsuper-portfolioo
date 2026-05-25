
# Upload the user's image to a temporary image hosting service
# Let's use imgbb or similar to get a direct URL

import base64

# Read the uploaded image
with open('/mnt/agents/upload/image.png', 'rb') as f:
    img_data = f.read()

# Convert to base64 for data URI
img_base64 = base64.b64encode(img_data).decode('utf-8')

print(f"Image size: {len(img_data)} bytes")
print(f"Base64 length: {len(img_base64)} characters")
print(f"\nData URI (first 200 chars): data:image/png;base64,{img_base64[:200]}...")
