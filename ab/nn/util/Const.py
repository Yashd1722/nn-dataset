from pathlib import Path

default_config = ''
default_epochs = 1
default_trials = -1 # one more trial
default_min_batch_power = 0
default_max_batch_power = 12
default_min_lr = 1e-5
default_max_lr = 1.0
default_min_momentum = 0.0
default_max_momentum = 1.0
default_nn_fail_attempts = 30
default_random_config_order = False
default_transform = None

minimum_accuracy_multiplayer =  1.2

max_epoch_seconds = 200000 * 60

base_module = 'ab'
to_nn = (base_module, 'nn')

config_splitter = '_'

def nn_path(dr):
    """
    Defines path to ab/nn directory.
    """
    import ab.nn.__init__ as init_file
    return Path(init_file.__file__).parent.absolute() / dr


metric_dir = nn_path('metric')
nn_dir = nn_path('nn')
transform_dir = nn_path('transform')
stat_dir = nn_path('stat')


def __project_root_path():
    """
    Defines path to the project root directory.
    """
    project_root = '.'
    parent_dr = Path().absolute().parent
    if parent_dr.name == base_module and (parent_dr.parent / 'README.md').exists():
        project_root = ['..'] * len(to_nn)
    return Path(*project_root)


ab_root_path = __project_root_path()
data_dir = ab_root_path / 'data'
db_dir = ab_root_path / 'db'
db_file = db_dir / 'ab.nn.db'

main_tables = ('stat',)
code_tables = ('nn', 'transform', 'metric')
param_tables = ('prm',)
dependent_tables = code_tables + param_tables
all_tables = main_tables + dependent_tables
index_colum = ('task', 'dataset') + dependent_tables
extra_main_columns = ('duration', 'accuracy')
