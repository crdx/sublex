# sublime-file-excluder

Sublime Text 3 does not have a way to hide files or directories from the tree based on the contents of the `.gitignore` file at the root of the currently-loaded project. This plugin adds that functionality.

## File support

Only `.gitignore` is supported at the moment, but in theory any project-level pattern-holding exclusion file is a candidate for inclusion.

## Ignoring patterns

It is possible to use a special comment to indicate that a certain pattern should be ignored by this plugin. For example you may not want to check in your `*.env` files, but still be able to view and edit them.

```bash
# sublime-file-excluder: ignore next
*.env
```

It is also possible to ignore the next `n` lines by specifying a number after `ignore next`. For example:

```bash
# sublime-file-excluder: ignore next 3
development.env
production.env
test.env
```

## How it works

The API allows us to extract out the `project_data` from the current window, and set the `file_exclude_patterns` and `folder_exclude_patterns` variables, in-memory.

The API does not support an event when a project is loaded, so the compromise is to refresh the state in response to the following two events:

- `on_activated_async`
- `on_post_save_async` when the current filename matches `.gitignore`

The refresh action has been kept extremely lightweight (one file read) so that calling it regularly is not intensive.

## Bugs or contributions

Open an [issue](http://github.com/crdx/sublime-file-excluder/issues) or send a [pull request](http://github.com/crdx/sublime-file-excluder/pulls).

## Licence

[MIT](LICENCE.md).
