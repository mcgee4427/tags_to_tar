# tags_to_tar
This script was created to make archive and hand off to a CPA easy and repeatable
without manual copies and duplicate files.

This script looks for json files matching the manifest filename found in the config
file.  It looks inside the manifest file and if the entity name matches the current
job it adds files in the same folder that match the file specs in the manifest file.

The filespec portion is a list and multiple filespecs can be added.

