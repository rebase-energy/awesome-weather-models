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
The weather models are categorized according metadata found in the [JSON schema](https://json-schema.org/) specification ([schema_ai_models.json](https://github.com/rebase-energy/awesome-weather-models/blob/main/schema_ai_models.json)). The table below (in alphabetical order) is extracted from the full categorization will columns defined as: 

* **Name**: Name of the weather model. 
* **Organization**: Organization that developed the weather model. 
* **Operational Data**: If forecast data from the model is provided at an operational basis.
* **Open Source**: If the source code is provided as open source. 
* **Open Weights**: If the model weights are provided as open weights. 

Click the link of the model name to see the full model categorization. 

| Name | Organization | Operational Data | Open Source | Open Weights | Links |
| :--- | :--- | :---: | :---: | :---: | :---: |
|[`AIFS`](L2-L27)|ECMWF|✅ <br> CC BY 4.0|❌|❌|[[paper]](https://arxiv.org/abs/2406.01465), [[access]](https://www.ecmwf.int/en/forecasts/dataset/aifs-machine-learning-data)|
|[`ARCHESWEATHER\-L`](L29-L55)|INRIA|❌|✅ <br> MIT|✅ <br> MIT|[[code]](https://github.com/gcouairon/ArchesWeather), [[paper]](https://arxiv.org/abs/2405.14527)|
|[`ARCHESWEATHER\-M`](L57-L83)|INRIA|❌|✅ <br> MIT|✅ <br> MIT|[[code]](https://github.com/gcouairon/ArchesWeather), [[paper]](https://arxiv.org/abs/2405.14527)|
|[`ARCHESWEATHER\-S`](L85-L111)|INRIA|❌|✅ <br> MIT|✅ <br> MIT|[[code]](https://github.com/gcouairon/ArchesWeather), [[paper]](https://arxiv.org/abs/2405.14527)|
|[`Aurora`](L113-L141)|Microsoft|❌|✅ <br> MIT|✅ <br> MIT|[[code]](https://github.com/microsoft/aurora), [[paper]](https://arxiv.org/abs/2405.13063), [[docs]](https://microsoft.github.io/aurora/intro.html), [[pypi]](https://pypi.org/project/microsoft-aurora/)|
|[`ClimaX\-H`](L143-L169)|Microsoft|❌|✅ <br> MIT|❌|[[code]](https://github.com/microsoft/ClimaX), [[paper]](https://arxiv.org/abs/2301.10343), [[docs]](https://microsoft.github.io/climax/intro.html)|
|[`ClimaX\-L`](L171-L197)|Microsoft|❌|✅ <br> MIT|❌|[[code]](https://github.com/microsoft/ClimaX), [[paper]](https://arxiv.org/abs/2301.10343), [[docs]](https://microsoft.github.io/climax/intro.html)|
|[`FengWu`](L199-L225)|OpenEarthLab|❌|✅ <br> MIT|✅ <br> None|[[code]](https://github.com/OpenEarthLab/FengWu), [[paper]](https://arxiv.org/abs/2304.02948)|
|[`FourCastNet`](L227-L253)|Nvidia|❌|✅ <br> BSD 3-Clause|✅ <br> BSD 3-Clause|[[code]](https://github.com/NVlabs/FourCastNet), [[paper]](https://arxiv.org/abs/2202.11214)|
|[`GraphCast`](L255-L282)|Google-DeepMind|❌|✅ <br> APACHE-2.0|✅ <br> CC BY-NC-SA 4.0|[[code]](https://github.com/deepmind/graphcast), [[paper]](https://arxiv.org/abs/2212.12794), [[blog]](https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/)|
|[`MET Norway`](L284-L307)|MET Norway|❌|❌|❌|[[paper]](https://arxiv.org/abs/2409.02891)|
|[`Pangu\-Weather`](L309-L335)|Huawei|❌|✅ <br> CC BY-NC-SA 4.0|✅ <br> CC BY-NC-SA 4.0|[[code]](https://github.com/198808xc/Pangu-Weather), [[paper]](https://arxiv.org/abs/2211.02556)|

## How to Contribute? 
Contributions are much welcome! 

1) Add a model to the list
2) Update categorization and links
3) Feedback on categorization/structure to make it more useful

Feel free to make a PR and we will incorporate it. 