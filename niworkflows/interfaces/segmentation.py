# -*- coding: utf-8 -*-
"""
ReportCapableInterfaces for segmentation tools


"""
from nipype.interfaces import fsl
from niworkflows.common import report as nrc
from niworkflows.viz.utils import plot_mask

class FASTInputSpecRPT(nrc.ReportCapableInputSpec,
                       fsl.preprocess.FASTInputSpec):
    pass

class FASTOutputSpecRPT(nrc.ReportCapableOutputSpec,
                        fsl.preprocess.FASTOutputSpec):
    pass

class FASTRPT(nrc.ReportCapableInterface, fsl.FAST):
    input_spec = FASTInputSpecRPT
    output_spec = FASTOutputSpecRPT

    def _generate_report(self):
        raise NotImplementedError


class BETInputSpecRPT(nrc.ReportCapableInputSpec,
                      fsl.preprocess.BETInputSpec):
    pass

class BETOutputSpecRPT(nrc.ReportCapableOutputSpec,
                       fsl.preprocess.BETOutputSpec):
    pass

class BETRPT(nrc.ReportCapableInterface, fsl.BET):
    input_spec = BETInputSpecRPT
    output_spec = BETOutputSpecRPT

    def _generate_report(self):
        ''' generates a report showing three orthogonal slices of an arbitrary
        volume of in_file, with the resulting binary brain mask overlaid '''

        plot_mask(
            self.inputs.in_file,
            self.aggregate_outputs().mask_file,
            out_file=self._out_report,
            ifinputs=self.inputs.get(),
            ifoutputs=self.aggregate_outputs()
        )
