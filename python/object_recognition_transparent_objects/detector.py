#!/usr/bin/env python
"""
Module defining the transparent objects detector to find objects in a scene
"""

from object_recognition_core.db import ObjectDb, Models
from object_recognition_core.pipelines.detection import DetectionPipeline
from object_recognition_core.utils import json_helper
import transparent_objects_cells

########################################################################################################################

class TransparentObjectsDetectionPipeline(DetectionPipeline):

    @classmethod
    def config_doc(cls):
        return  """
                parameters:
                    # The path of the 'registrationMask_SXGA.png' given in the conf folder
                    registrationMaskFilename: '/tmp/registrationMask_SXGA.png'
                    # The usual parameters for the DB
                    db:
        """

    @classmethod
    def type_name(cls):
        return 'transparent_objects'

    @classmethod
    def detector(self, *args, **kwargs):
        visualize = kwargs.pop('visualize', False)
        subtype = kwargs.pop('subtype')
        parameters = kwargs.pop('parameters')
        object_ids = parameters['object_ids']
        object_db = ObjectDb(parameters['db'])
        model_documents = Models(object_db, object_ids, self.type_name(), json_helper.dict_to_cpp_json_str(subtype))
        registrationMaskFilename = parameters.get('registrationMaskFilename')
        return transparent_objects_cells.Detector(model_documents=model_documents, object_db=object_db,
                                            registrationMaskFilename=registrationMaskFilename, visualize=visualize)
