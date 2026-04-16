# mti-radar-signal-processor
# MTI Radar Signal Processor

End-to-end implementation of a Moving Target Indicator (MTI) radar signal processing chain, simulating detection of moving targets in the presence of ground clutter.

##Overview

This project models a classical pulsed radar processing pipeline, focusing on clutter suppression and target detection using MTI filtering and Doppler processing.

#Processing Pipeline

Waveform Generation -> Clutter & Target Simulation -> MTI Filtering -> Range-Doppler Processing -> CFAR Detection


## Pipeline
- Waveform Generation (Pulsed radar, PRF design, Staggered PRF)
- Target + Clutter Simulation (Doppler, RCS)
- MTI Filter (Delay line canceller)
- CFAR Detection (CA-CFAR)
- Visualization (Range-Doppler map, Detection plot)

## Key Outputs

- Range-Doppler maps
- Clutter suppression using MTI
- Detection performance under varying SCR


## Reference
Mahafza - Radar Systems Analysis and Design Using MATLAB
