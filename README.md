# Blankslate

![Continuous Integration (CI) Tests](https://github.com/unkokaeru/blankslate/actions/workflows/continuous_integration.yml/badge.svg)

Generates a blankslate for a new Python project. Recommended to use the [Blankslate Extension Pack](https://marketplace.visualstudio.com/items?itemName=unkokaeru.blankslate-extension-pack).

Uses Angular Commit Style:

```plaintext
<type>(<scope>): <short summary>
    │       │             │
    │       │             └─⫸ Summary in present tense. Not capitalized. No period at the end.
    │       │
    │       └─⫸ Commit Scope: animations|bazel|benchpress|common|compiler|compiler-cli|core|
    │                          elements|forms|http|language-service|localize|platform-browser|
    │                          platform-browser-dynamic|platform-server|router|service-worker|
    │                          upgrade|zone.js|packaging|changelog|docs-infra|migrations|ngcc|ve|
    │                          devtools
    │
    └─⫸ Commit Type: build|ci|docs|feat|fix|perf|refactor|test
```

**Currently in developement.**