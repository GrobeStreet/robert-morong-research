# Robert Morong Research

[![Netlify Status](https://api.netlify.com/api/v1/badges/9ad0dce5-6638-4d05-af4a-9ef28bcb91ec/deploy-status)](https://app.netlify.com/projects/robert-morong-research/deploys)
[![Source: GitHub main](https://img.shields.io/badge/source-GitHub_main-78e6c4.svg)](https://github.com/GrobeStreet/robert-morong-research)
[![License: MIT](https://img.shields.io/badge/license-MIT-2a3b55.svg)](LICENSE)

Canonical source for Robert Morong's public research website.

Production: [robert-morong-research.netlify.app](https://robert-morong-research.netlify.app)

The site is intentionally static: `index.html` is the publishable artifact, and
`netlify.toml` records the production configuration. Research claims should be
updated here, reviewed against their linked result repositories, committed to
`main`, and only then deployed to Netlify.

## Local preview

```sh
python3 -m http.server 8080
```

## Production deploy

```sh
npx netlify deploy --prod --dir .
```

The local checkout must be linked to the existing Netlify site before deploying.
