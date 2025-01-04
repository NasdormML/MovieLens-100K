import joblib
import os


model_path = 'models/hybrid_als.pkl'
saved_model_path = 'models/hybrid_als.pkl'

os.makedirs(os.path.dirname(saved_model_path), exist_ok=True)
joblib.dump(model_path, saved_model_path)
print(f"Model saved to {saved_model_path}")
