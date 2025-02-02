# Customize the folder, sub-folders, and filenames of your images! 
# Save data about the generated job (sampler, prompts, models) as entries in a `json` (text) file, in each folder.
# Use the values of ANY node's widget, by simply adding its badge number in the form _id.widget_name_: 
# Oh btw... also saves your output as **WebP** or **JPEG**... And yes the prompt is included :) ComfyUI can load it but a PR approval is needed.

"""
@author: AudioscavengeR
@title: Save Image Extended
@nickname: Save Image Extended
@description: 1 custom node to save your pictures in various folders and formats.
"""


from .save_image_extended import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
