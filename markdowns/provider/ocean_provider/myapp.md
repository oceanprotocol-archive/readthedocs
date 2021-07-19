---
title: myapp
slug: ocean_provider/myapp
app: provider
module: ocean_provider.myapp
source: https://github.com/oceanprotocol/provider/blob/issue-182-improve-docs/ocean_provider/myapp.py
version: 0.4.12
---
This module creates an instance of flask `app`, creates `user_nonce` table if not exists, and sets the environment configuration.
If `CONFIG_FILE` is not found in environment variables, default `config.ini` file is used.

