config = {
    'exp_name': "finetune_bert",
    'bert_arch': 'bert-base-multilingual-cased',
    'epochs': 3,
    'batch_size': 8,
    'lr': 5e-5,
    'valid_freq': 50, 
    'save_freq': 100,
    'device': 'cpu',
    'data_dir': "data/",
    'max_grad_norm': 1.0,
    'weight_decay': 0.0,
    'adam_epsilon': 1e-8,
    'warmup_steps': 0,
}