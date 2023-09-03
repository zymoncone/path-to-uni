#For training predictive model, because the dataset collected this model was not fully trained due to lack of time based data.
import pandas as pd
import taipy as tp
import numpy as np
import datetime as dt
from taipy import Config, Scope

file_path = r"data/College_Admissions.csv"

dataset = pd.read_csv(file_path)
print(dataset.head())

## Input Data Nodes
initial_dataset_cfg = Config.configure_data_node(id="initial_dataset",
                                                 storage_type="csv",
                                                 path=file_path,
                                                 scope=Scope.GLOBAL)

# Corrected default_data argument for GPA
gpa_cfg = Config.configure_data_node(id="gpa", default_data=4)

n_predictions_cfg = Config.configure_data_node(id="n_predictions", default_data=5)

max_capacity_cfg = Config.configure_data_node(id="max_capacity", default_data=181)

## Remaining Data Nodes
# Corrected validity_period to use timedelta
cleaned_dataset_cfg = Config.configure_data_node(id="cleaned_dataset",
                                             cacheable=True,
                                             validity_period=dt.timedelta(days=1),  # Corrected validity_period
                                             scope=Scope.GLOBAL)

predictions_cfg = Config.configure_data_node(id="predictions", scope=Scope.PIPELINE)

def clean_data(initial_dataset):
    print("     Cleaning data")
    # No need for pd.to_numeric here
    cleaned_dataset = initial_dataset.copy()
    return cleaned_dataset

def predict_baseline(cleaned_dataset, n_predictions, gpa, max_capacity):
    print("     Predicting baseline")
    # No need for pd.to_numeric here
    train_dataset = cleaned_dataset[cleaned_dataset["GPA"] < 4]

    predictions = train_dataset["GPA"][-n_predictions:].reset_index(drop=True)
    predictions = predictions.apply(lambda x: min(x, max_capacity))
    return predictions

# Create the task configurations
clean_data_task_cfg = Config.configure_task(id="clean_data",
                                            function=clean_data,
                                            input=initial_dataset_cfg,
                                            output=cleaned_dataset_cfg)

predict_baseline_task_cfg = Config.configure_task(id="predict_baseline",
                                                  function=predict_baseline,
                                                  input=[cleaned_dataset_cfg, n_predictions_cfg, gpa_cfg, max_capacity_cfg],
                                                  output=predictions_cfg)

# Create the first pipeline configuration
baseline_pipeline_cfg = Config.configure_pipeline(id="baseline",
                                                  task_configs=[clean_data_task_cfg, predict_baseline_task_cfg])

# Create the pipeline
baseline_pipeline = tp.create_pipeline(baseline_pipeline_cfg)

# Submit the pipeline (Execution)
tp.submit(baseline_pipeline)

# Read output data from the pipeline
baseline_predictions = baseline_pipeline.predictions.read()
print("Predictions of baseline algorithm\n", baseline_predictions)

#For GUI and Pipelines
'''# Initialize the "predictions" dataset
predictions_dataset = pd.DataFrame({"GPA":[1], "Historical values":[np.NaN], "Predicted values":[np.NaN]})

# Add a button and a chart for our predictions
pipeline_page = page + """
Press <|predict|button|on_action=predict|> to predict with default parameters (30 predictions) and June 1st as day.

<|{predictions_dataset}|chart|x=Date|y[1]=Historical values|type[1]=bar|y[2]=Predicted values|type[2]=scatter|height=80%|width=100%|>
"""

def predict(state):
    print("'Predict' button clicked")
    pipeline = create_and_submit_pipeline()
    update_predictions_dataset(state, pipeline)


def create_and_submit_pipeline():
    print("Execution of pipeline...")
    # Create the pipeline from the pipeline config
    pipeline = tp.create_pipeline(baseline_pipeline_cfg)
    # Submit the pipeline (Execution)
    tp.submit(pipeline)
    return pipeline'''