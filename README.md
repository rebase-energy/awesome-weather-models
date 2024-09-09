<h1 align="center">
    🌦️ awesome-weather-models
    <br>
</h1>

<p align="center">
    <strong>A catalogue and categorization of AI-based weather forecasting models. 
   </strong>
</p>

## Why this Page?
This page provide a catalogue and categorization of AI-based weather forecasting models. The aim is that this page will enable discovery and comparison of the different available model options. 

## Weather Models
The weather models are categorized according meta data found in the JSON schema specification ([schema_ai_models.json](https://github.com/rebase-energy/awesome-weather-models/blob/main/schema_ai_models.json)). Below is a table in alphabetical order extracted from the full categorization providing name, description and if it is an open model. 

* **Operational Data**: Forecast data from the model is provided at an operational basis.
* **Open Source**: The source code is provided as open source. 
* **Open Weights**: The model weights are provided as open weights. 

| Name | Description | Operational Data | Open Source | Open Weights | Links |
| :--- | :--- | :---: | :---: | :---: | :---: |
|`AIFS`|AIFS is an AI-based global weather forecasting model that uses a graph neural network (GNN) with a transformer-based processor to produce medium-range forecasts.|✅ <br> CC BY 4.0|❌|❌|[[paper]](https://arxiv.org/abs/2406.01465), [[access]](https://www.ecmwf.int/en/forecasts/dataset/aifs-machine-learning-data)|
|`ARCHESWEATHER-L`|AI-based weather forecasting model using a transformer architecture with Cross-Level Attention for efficient global weather prediction.|❌|✅ <br> MIT|✅ <br> MIT|[[code]](https://github.com/gcouairon/ArchesWeather), [[paper]](https://arxiv.org/abs/2405.14527)|
|`ARCHESWEATHER-M`|AI-based weather forecasting model using a transformer architecture with Cross-Level Attention for efficient global weather prediction.|❌|✅ <br> MIT|✅ <br> MIT|[[code]](https://github.com/gcouairon/ArchesWeather), [[paper]](https://arxiv.org/abs/2405.14527)|
|`ARCHESWEATHER-S`|AI-based weather forecasting model using a transformer architecture with Cross-Level Attention for efficient global weather prediction.|❌|✅ <br> MIT|✅ <br> MIT|[[code]](https://github.com/gcouairon/ArchesWeather), [[paper]](https://arxiv.org/abs/2405.14527)|
|`Aurora`|Aurora is an AI-based model that generates global weather and air pollution forecasts. It utilizes 3D Swin Transformer architecture and is pre-trained on diverse atmospheric data.|❌|✅ <br> MIT|✅ <br> MIT|[[code]](https://github.com/microsoft/aurora), [[paper]](https://arxiv.org/abs/2405.13063), [[docs]](https://microsoft.github.io/aurora/intro.html), [[pypi]](https://pypi.org/project/microsoft-aurora/)|
|`ClimaX-H`|ClimaX high resolution foundation model for weather forecasting to and climate projections, using a vision transformer architecture.|❌|✅ <br> MIT|❌|[[code]](https://github.com/microsoft/ClimaX), [[paper]](https://arxiv.org/abs/2301.10343), [[docs]](https://microsoft.github.io/climax/intro.html)|
|`ClimaX-L`|ClimaX low resolution foundation model for weather forecasting to and climate projections, using a vision transformer architecture.|❌|✅ <br> MIT|❌|[[code]](https://github.com/microsoft/ClimaX), [[paper]](https://arxiv.org/abs/2301.10343), [[docs]](https://microsoft.github.io/climax/intro.html)|
|`FengWu`|AI-based global medium-range weather forecasting system using a multi-modal and multi-task learning approach, trained on ERA5 data to predict atmospheric conditions with 0.25° resolution.|❌|✅ <br> MIT|✅ <br> None|[[code]](https://github.com/OpenEarthLab/FengWu), [[paper]](https://arxiv.org/abs/2304.02948)|
|`FourCastNet`|Global AI-based weather forecasting model that uses Adaptive Fourier Neural Operators to produce high-resolution short to medium-range forecasts.|❌|✅ <br> BSD 3-Clause|✅ <br> BSD 3-Clause|[[code]](https://github.com/NVlabs/FourCastNet), [[paper]](https://arxiv.org/abs/2202.11214)|
|`GraphCast`|AI-based medium-range global weather forecasting with 3D neural networks.|❌|✅ <br> APACHE-2.0|✅ <br> CC BY-NC-SA 4.0|[[code]](https://github.com/deepmind/graphcast), [[paper]](https://arxiv.org/abs/2212.12794), [[blog]](https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/)|
|`MET Norway`|A regional data-driven weather model with a global stretched-grid architecture, focusing on high-resolution forecasting for the Nordics, while maintaining lower resolution globally.|❌|❌|❌|[[paper]](https://arxiv.org/abs/2409.02891)|
|`Pangu-Weather`|AI-based global weather forecasting system that uses a 3D Earth-specific transformer architecture to provide short to medium-range forecasts.|❌|✅ <br> CC BY-NC-SA 4.0|✅ <br> CC BY-NC-SA 4.0|[[code]](https://github.com/198808xc/Pangu-Weather), [[paper]](https://arxiv.org/abs/2211.02556)|

## How to Contribute? 
Contributions are much welcome! 

1) Add a model to the list
2) Update categorization and links
3) Feedback on categorization/structure to make it more useful

Feel free to make a PR and we will incorporate it. 