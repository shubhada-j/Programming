# How MAE work  (used for regression problem)

def Marvellous_MAE(Y_True, Y_Pred):
    n = len(Y_Pred)
    total_error = 0

    for i in range(n):
        error =abs(Y_True[i] - Y_Pred[i])
        total_error = total_error + error

    MAE = total_error / n
    return MAE

Y_True = [10,20,30]         #expected
Y_Pred = [12,18,33]         #predicted

loss = Marvellous_MAE(Y_True,Y_Pred)

print("Loss is : ",loss)