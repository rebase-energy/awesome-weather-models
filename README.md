<h1 align="center">
    🌦️ awesome-weather-models
    <br>
    <a href="https://github.com/sindresorhus/awesome">
        <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome">
    </a>
</h1>

<p align="center">
    <strong>A catalogue and categorization of AI-based weather forecasting models. 
   </strong>
</p>

## Why this Page?
This page provide a catalogue and categorization of AI-based weather forecasting models. The aim is that this page will enable discovery and comparison of the different available model options. 

## Weather Models
The weather models are categorized according metadata found in the [JSON schema](https://json-schema.org/) specification ([schema_ai_models.json](https://github.com/rebase-energy/awesome-weather-models/blob/main/schema_ai_models.json)). The table below (in alphabetical order) is extracted from the full categorization with columns defined as: 

* **Name**: Name of the weather model. 
* **Organization**: Organization that developed the weather model. 
* **Operational Data**: If forecast data from the model is provided at an operational basis.
* **Open Source**: If the source code is provided as open source. 
* **Open Weights**: If the model weights are provided as open weights. 

Click the link of the model name to see the full model categorization. 

| Name | Organization | Operational Data | Open Source | Open Weights | Links |
| :--- | :--- | :---: | :---: | :---: | :---: |
|[`AIFS`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json#L2-L28)|ECMWF|✅ <br> CC BY 4.0|❌|❌|[[paper]](https://arxiv.org/abs/2406.01465), [[access]](https://www.ecmwf.int/en/forecasts/dataset/aifs-machine-learning-data)|
|[`ARCHESWEATHER‑L`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json#L29-L56)|INRIA|❌|✅ <br> MIT|✅ <br> MIT|[[code]](https://github.com/gcouairon/ArchesWeather), [[paper]](https://arxiv.org/abs/2405.14527)|
|[`ARCHESWEATHER‑M`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json#L57-L84)|INRIA|❌|✅ <br> MIT|✅ <br> MIT|[[code]](https://github.com/gcouairon/ArchesWeather), [[paper]](https://arxiv.org/abs/2405.14527)|
|[`ARCHESWEATHER‑S`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json#L85-L112)|INRIA|❌|✅ <br> MIT|✅ <br> MIT|[[code]](https://github.com/gcouairon/ArchesWeather), [[paper]](https://arxiv.org/abs/2405.14527)|
|[`Aurora`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json#L113-L142)|Microsoft|❌|✅ <br> MIT|✅ <br> MIT|[[code]](https://github.com/microsoft/aurora), [[paper]](https://arxiv.org/abs/2405.13063), [[docs]](https://microsoft.github.io/aurora/intro.html), [[pypi]](https://pypi.org/project/microsoft-aurora/)|
|[`ClimaX‑H`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json#L143-L170)|Microsoft|❌|✅ <br> MIT|❌|[[code]](https://github.com/microsoft/ClimaX), [[paper]](https://arxiv.org/abs/2301.10343), [[docs]](https://microsoft.github.io/climax/intro.html)|
|[`ClimaX‑L`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json#L171-L198)|Microsoft|❌|✅ <br> MIT|❌|[[code]](https://github.com/microsoft/ClimaX), [[paper]](https://arxiv.org/abs/2301.10343), [[docs]](https://microsoft.github.io/climax/intro.html)|
|[`FengWu`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json#L199-L226)|OpenEarthLab|❌|✅ <br> MIT|✅ <br> None|[[code]](https://github.com/OpenEarthLab/FengWu), [[paper]](https://arxiv.org/abs/2304.02948)|
|[`FourCastNet`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json#L227-L254)|Nvidia|❌|✅ <br> BSD 3-Clause|✅ <br> BSD 3-Clause|[[code]](https://github.com/NVlabs/FourCastNet), [[paper]](https://arxiv.org/abs/2202.11214)|
|[`GraphCast`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json#L255-L283)|Google-DeepMind|❌|✅ <br> APACHE-2.0|✅ <br> CC BY-NC-SA 4.0|[[code]](https://github.com/deepmind/graphcast), [[paper]](https://arxiv.org/abs/2212.12794), [[blog]](https://deepmind.google/discover/blog/graphcast-ai-model-for-faster-and-more-accurate-global-weather-forecasting/)|
|[`MET Norway`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json#L284-L308)|MET Norway|❌|❌|❌|[[paper]](https://arxiv.org/abs/2409.02891)|
|[`Pangu‑Weather`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json#L309-L336)|Huawei|❌|✅ <br> CC BY-NC-SA 4.0|✅ <br> CC BY-NC-SA 4.0|[[code]](https://github.com/198808xc/Pangu-Weather), [[paper]](https://arxiv.org/abs/2211.02556)|
|[`Prithvi WxC`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json#L337-L365)|IBM and NASA|❌|✅ <br> MIT|✅ <br> MIT|[[code]](https://github.com/NASA-IMPACT/Prithvi-WxC), [[paper]](https://arxiv.org/abs/2409.13598), [[weights]](https://huggingface.co/Prithvi-WxC)|

## How to Contribute? 
Contributions are much welcome! 

* Add a model to the list
* Update categorization and links
* Feedback on categorization/structure to make it more useful

Feel free to make a PR or issue and we will incorporate it. 

For making PRs, here is how to make changes to the repo: 

1) All updates/changes should be done to the following files: 
* [`data_ai_models.json`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json) for updates/changes to model categorization.
* [`schema_ai_models.json`](https://github.com/rebase-energy/awesome-weather-models/blob/main/schema_ai_models.json) for schema changes.
* [`README_no_table.md`](https://github.com/rebase-energy/awesome-weather-models/blob/main/README_no_table.md) for changes to the README. 

2) When updates/changes are completed run `python validate_convert_insert.py`. Make sure all JSON validations checks pass. 

3) The files [`ai_model.md`](https://github.com/rebase-energy/awesome-weather-models/blob/main/ai_models.md) and [´README.md´](https://github.com/rebase-energy/awesome-weather-models/blob/main/README.md) will be auto-generated from the script. 

4) Add all the changed and generated files and submit the PR. 