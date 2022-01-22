# %% [code] {"jupyter":{"outputs_hidden":false}}
import optuna
import lightgbm as lgbm


def objective(trial,data=dataX,target=dataY):
    
    train_x, test_x, train_y, test_y = train_test_split(data, target, test_size=0.2,random_state=42)
    param =   {
        'num_leaves': trial.suggest_int('num_leaves', 2, 256),
        'objective': 'regression',
        'max_depth': -1,
        'learning_rate': 0.1,
        "boosting": "gbdt",
        'lambda_l1': trial.suggest_loguniform('lambda_l1', 1e-8, 10.0),
        'lambda_l2': trial.suggest_loguniform('lambda_l2', 1e-8, 10.0),
        "bagging_freq": 5,
        "bagging_fraction": trial.suggest_uniform('bagging_fraction', 0.1, 1.0),
        "feature_fraction": trial.suggest_uniform('feature_fraction', 0.4, 1.0),
        "verbosity": -1,
    }
    model = lgb.LGBMClassifier(**param)      
    model.fit(train_x,train_y,eval_set=[(test_x,test_y)],early_stopping_rounds=100,verbose=False)
    preds = model.predict(test_x)
    rmse = mean_squared_error(test_y, preds,squared=False)
    
    return rmse


def main():
    study = optuna.create_study(direction='minimize')
    study.optimize(objective, n_trials=5)
    Best_trial=study.best_trial.params
    print(Best_trial)

    
if __name__ == '__main__':
    main()