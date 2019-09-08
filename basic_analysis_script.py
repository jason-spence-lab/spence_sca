'''
BASIC SINGLE CELL ANALYSIS SCRIPT
by Josh Wu
4 June, 2019

Relies heavily on the Scanpy Python module developed by the Theis Lab
Read more about Scanpy at https://scanpy.readthedocs.io/en/latest/index.html

Contains analysis of kidney samples obtained by Emily Holloway
Template for a Basic Analysis 

Utilises dictionaries to store parameters for analysis, calling functions from scanpy_spence.py file in ./tools
Will be moving to encapsulate analysis parameters and functions using class sca_set
'''

import tools.scanpy_spence as sca

figdir = './figures/'
sca_dict = dict()

#############################################################################
## Change this to point toward your mount location for our MiStorage share ##
#############################################################################
sca_dict.update(storage_mount_point = 'Z:/')

## IDs of samples as represented in the metadata table
sca_dict.update(sample_list = ['2757-1','2761-1']) # Kidney data

sca_dict.update(gene_lists = ['basic_marker_list'])

## List of interesting genes
sca_dict.update(basic_marker_list = dict(markers = ['CDH5','KDR','FLT1','NOS3','VWF','EMCN','CDH1','KRT8','EPCAM','ITGAM',
													'PTPRC','COL1A1','COL1A2','PDGFRA','S100B','STMN2','TUBB3'],
										 positions=None, groups=None))

## Parameters used to filter the data - Mainly used to get rid of bad cells
sca_dict.update(filter_params = dict(min_cells = 0, # Filter out genes expressed in fewer cells
								min_genes = 500, # Filter out cells with fewer genes to remove dead cells
								max_genes = 7000, # Filter out cells with more genes to remove most doublets
								max_counts = 30000, # Filter out cells with more UMIs to catch a few remaining doublets
								max_mito = 0.15)) # Filter out cells with high mitochondrial gene content

## Settings for plotting
sca_dict.update(plot_params = dict(size = 20, # Size for dots of UMAP plots
								   umap_obs = ['louvain','sampleName'], # Observations to view on UMAP plots
								   exp_grouping = ['louvain'])) # Observations to group by within dot plots, heat maps, etc.

## Parameters used for initial clustering analysis
sca_dict.update(analysis_params = dict(n_neighbors = 15, # Size of the local neighborhood used for manifold approximation
								n_pcs = 11, # Number of principle components to use in construction of neighborhood graph
								spread = 1, # In combination with min_dist determines how clumped embedded points are
								min_dist = 0.4, # Minimum distance between points on the umap graph
								resolution = 0.5)) # High resolution attempts to increases # of clusters identified

## Basic pipeline for analysis - will filter data, process, cluster, etc. and output relevant figures
sca.pipe_basic(sca_dict,figdir)#,load_save='adata_save.p')


## If you find some interesting clusters that you want to "zoom in" on and recluster, you can use the following code

# New analysis parameters for the subset of parameters
# analysis_params_ext = dict(n_neighbors = 9,
# 						n_pcs = 10,
# 						spread = 1,
# 						min_dist = 0.4,
# 						resolution = 0.4)

# sca.pipe_ext(sca_dict,analysis_params_ext, figdir=figdir, extracted=2)#, load_save='adata_save.p')

