
from training.trainingModel import trainModel
from training.training_Validation_Insertion import train_validation







def trainRouteClient(folderPath):

    try:
            train_valObj = train_validation(folderPath) #object initialization
            print("Done1")
            train_valObj.train_validation()#calling the training_validation function
            print("Done2")

            trainModelObj = trainModel() #object initialization
            print("Done3")
            trainModelObj.trainingModel() #training the model for the files in the table
            print("Done4")
    except ValueError:

        return "Error Occurred! %s" % ValueError

    except KeyError:

        return "Error Occurred! %s" % KeyError

    except Exception as e:

        return "Error Occurred! %s" % e
    print("Done")
    return "Training successfull!!"

if __name__ == "__main__":
     trainRouteClient("Training_Batch_Files")