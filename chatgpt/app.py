from deepface import DeepFace

# Load the pre-trained model
model = DeepFace.build_model('Facenet')

# Perform face recognition
result = DeepFace.verify("img1.jpg", "img2.jpg", model_name='Facenet')

# Print the result
print(result)
