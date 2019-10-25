inputs = [0,0,1,0]
weights = [0,0,0,0]
indexs = [0,1,2,3]
desiredResult = 1
learningRate = 0.20
trials = 6

def learn(inputVector, weightVector):
    for index, inputValue, inputWeight in zip(indexs, inputVector, weightVector):
        if (inputValue > 0):
            weights[index] = (inputWeight + learningRate)
        else:
            weights[index] = (inputWeight)

def evauatedNeuralNetworkError(desired, actual):
    return (desired - actual)

def evaluatedNeuralNetwork(inputVector, weightVector):
    result = 0
    for inputValue, inputWeight in zip(inputVector, weightVector):
        layerValue = inputValue * inputWeight
        result += layerValue
    return result

def train(repeats):
    for i in range(repeats):
        neuralNetworkResult = evaluatedNeuralNetwork(inputs, weights)
        neuralNetError = evauatedNeuralNetworkError(desiredResult, neuralNetworkResult)
        print("NeuralNet Result:", neuralNetworkResult, "Error:", neuralNetError, "Weights:", weights)
        learn(inputs, weights)

print("Original Values")
neuralNetworkResult = evaluatedNeuralNetwork(inputs, weights)
neuralNetError = evauatedNeuralNetworkError(desiredResult, neuralNetworkResult)
print(inputs, weights)
print("NeuralNet Result:", neuralNetworkResult, "Error:", neuralNetError)

print("\n")

("Pós learning values")
learn(inputs, weights)
neuralNetworkResult = evaluatedNeuralNetwork(inputs, weights)
neuralNetError = evauatedNeuralNetworkError(desiredResult, neuralNetworkResult)
print(inputs, weights)
print("NeuralNet Result:", neuralNetworkResult, "Error:", neuralNetError)

print("\n")

train(trials);