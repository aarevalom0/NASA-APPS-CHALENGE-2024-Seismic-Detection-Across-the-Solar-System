# Welcome to Codex programl! 🌌

Dive into our cutting-edge IA model for detecting seismic signals! With impressive performance metrics and stunning visualizations, this project showcases how technology can enhance our understanding of detection of sismic activity. 🚀

## What to Expect from the Model 🌍

When you feed a CSV file into the model, it will provide the number of detected seismic events along with significant data. Additionally, it generates visualizations to help you understand the seismic activity better.

### Visualization Example

<img src="Plots/prediction/prediction%20XB.ELYSE.02.BHV.2022-01-02HR04_evid0006.png" alt="Prediction Plot" width="600"/>


In this graph, you can see the exact points of seismic events and their corresponding frequency. The beauty of this predictive model lies in its adaptability; it can continuously evolve as new data is introduced, ensuring that the detection process remains accurate and up-to-date.

## Key Features

- **High Accuracy**: The model consistently achieves high training and cross-validation scores (around 0.999-1.000), indicating excellent performance.
- **Robustness**: The close alignment of training and validation scores suggests that the model is not overfitting.

### Graph Explanation

<img src="Plots/Report%20Model/Learning%20curve.png" alt="Learning Curve" width="600"/>

This graph illustrates how the model's performance changes as the number of training instances increases. It effectively demonstrates the model's capacity to generalize well with an increasing amount of data.

## Data Analysis Plus 📊

This section highlights a significant plus: our approach goes beyond the initial goal of merely detecting seismic events. We provide a comprehensive HTML report filled with valuable insights that enhance our understanding of seismic activity.

For example, one of the plots shows velocity over time, effectively distinguishing between seismic events (blue) and noise (red). This visualization not only identifies seismic occurrences but also offers critical information about their characteristics. 

<img src="Plots/Statistics/Scatter%20Plot%20with%20Trend%20Lines%20Velocity%20Vs.%20Time.png" alt="Velocity Vs. Time" width="600"/>

In Graph , there’s a clear class imbalance, with many more noise data points than seismic events. Seismic events generally have lower velocity amplitudes compared to noise. Several noise spikes are visible, particularly around 40,000 and 80,000 seconds.

## Confusion Matrix 🧩

Notably, our model displays values in the confusion matrix that are even better than expected, showcasing its exceptional performance in detecting seismic signals. 

<img src="Plots/Report%20Model/Confusion%20Matrix.png" alt="Confusion Matrix" width="600"/>

- **True Positives (TP)**: The model's ability to correctly identify seismic events, which is critical for ensuring safety and prompt response measures.
- **False Positives (FP)**: These represent instances where noise is incorrectly classified as seismic events. Understanding and minimizing these can prevent unnecessary alerts and resource allocation.
- **False Negatives (FN)**: This is particularly concerning as it indicates missed seismic events, which could have severe consequences in real-world applications.







## Guide to Using a Model in a `.ipynb` Repository

To use the model contained in the `.ipynb` file, follow these steps:

### 1. Open the Jupyter Notebook

1. Start Jupyter Notebook in your working environment.
2. Navigate to the location of the `.ipynb` file containing the model.
3. Click on the file to open it.

### 2. Run the Notebook Cells

Once the notebook is open, you can run the cells in the following ways:

- **Run a single cell**: Select the cell you want to execute and press `Shift + Enter`. This will run the current cell and select the next one.
- **Run all cells**: Go to the menu and select `Cell` -> `Run All`. This will execute all cells in the notebook in order, from the first to the last.

### Note

Make sure that all necessary dependencies and libraries are installed before running the notebook. You can refer to the `requirements.txt` file to see which packages are needed and ensure they are installed in your environment.

