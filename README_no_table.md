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

<!-- table_placeholder -->

## How to Contribute? 
Contributions are much welcome! Make a PR or issue and we will incorporate it. Contributions could for example be: 

* Add a model to the list
* Update categorization and links
* Feedback on categorization/structure to make it more useful

When making a PR, follow the these steps to make sure your contribution is consistent with this repo structure: 

1) All updates/changes should be done to the following files: 
* [`data_ai_models.json`](https://github.com/rebase-energy/awesome-weather-models/blob/main/data_ai_models.json) for updates/changes to model categorization.
* [`schema_ai_models.json`](https://github.com/rebase-energy/awesome-weather-models/blob/main/schema_ai_models.json) for schema changes.
* [`README_no_table.md`](https://github.com/rebase-energy/awesome-weather-models/blob/main/README_no_table.md) for changes to the README. 

2) When updates/changes are completed run `python validate_convert_insert.py`. Make sure all JSON validations checks pass. 

3) The files [`ai_model.md`](https://github.com/rebase-energy/awesome-weather-models/blob/main/ai_models.md) and [´README.md´](https://github.com/rebase-energy/awesome-weather-models/blob/main/README.md) will be auto-generated from the script. 

4) Add all the changed and generated files and submit the PR. 