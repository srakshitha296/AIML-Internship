
import pickle


#load the pickle file
with open("C:\\Users\\sraks\\AIML Internship\\AIML-Internship\\TASK\\T01\\prediction.pickle", 'rb') as f:
    model = pickle.load(f)

predicted = model.predict([[0,0,1,1,69.0,1,1,1,1,2,2,1,0,2,2,0,1,61.40,0]])
print(predicted)