# sublime-file-excluder

Sublime Text 3 does not have a way to hide files or directories from the tree based on the contents of the `.gitignore` file at the root of the currently-loaded project. This plugin adds that functionality.

## How it works

The API allows us to extract out the `project_data` from the current window, and set the `file_exclude_patterns` and `folder_exclude_patterns` variables, in-memory.

The API does not support an event when a project is loaded, so the compromise is to refresh the state in response to the following two events:

- `on_activated_async`
- `on_post_save_async` when the current filename matches `.gitignore`

The refresh action has been kept extremely lightweight (one file read) so that calling it regularly is not intensive.

To work out the difference between a folder and a file **the trailing slash (`/`) in your .gitignore is significant**. If you find the plugin is not working correclty, ensure that all your exclusions have trailing slashes where needed.

## Supported files

Only `.gitignore` is supported at the moment, but in theory any project-level pattern-holding exclusion file is a candidate for inclusion.

## Bugs or contributions

Open an [issue](http://github.com/crdx/sublime-file-excluder/issues) or send a [pull request](http://github.com/crdx/sublime-file-excluder/pulls).

## Licence

[MIT](LICENCE.md).
