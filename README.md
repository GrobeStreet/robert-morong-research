# Robert Morong Research

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
