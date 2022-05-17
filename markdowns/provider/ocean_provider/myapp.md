---
title: myapp
slug: ocean_provider/myapp
app: provider
module: ocean_provider.myapp
source: https://github.com/oceanprotocol/provider/blob/v1.0.9/ocean_provider/myapp.py
version: 1.0.9
---
This module creates an instance of flask `app`, creates `user_nonce` table if not exists, and sets the environment configuration.
If `PROVIDER_CONFIG_FILE` is not found in environment variables, default `config.ini` file is used.

