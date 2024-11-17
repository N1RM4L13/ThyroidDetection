
from training.trainingModel import trainModel
from training.training_Validation_Insertion import train_validation
from prediction.prediction_Validation_Insertion import pred_validation
from prediction.predictModel import prediction

def trainRouteClient(folderPath):

    try:
            train_valObj = train_validation(folderPath) #object initialization
            train_valObj.train_validation()#calling the training_validation function

            trainModelObj = trainModel() #object initialization
            trainModelObj.trainingModel() #training the model for the files in the table

    except ValueError:

        return "Error Occurred! %s" % ValueError

    except KeyError:

        return "Error Occurred! %s" % KeyError

    except Exception as e:

        return "Error Occurred! %s" % e
    return "Training successfull!!"


def predictRouteClient(path):
    try:

            pred_val = pred_validation(path) #object initialization

            pred_val.prediction_validation() #calling the prediction_validation function

            pred = prediction(path) #object initialization

            # predicting for dataset present in database
            path = pred.predictionFromModel()
            print("Prediction File created at %s!!!" % path)

    except ValueError:
        print("Error Occurred! %s" %ValueError)
    except KeyError:
        print("Error Occurred! %s" %KeyError)
    except Exception as e:
        print("Error Occurred! %s" %e)

if __name__ == "__main__":
     predictRouteClient("Prediction_Batch_Files")