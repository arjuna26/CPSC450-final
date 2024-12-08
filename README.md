### Local Test Setup Instructions

#### Create Virtual Python Envrionment
```bash
python -m venv venv
```

#### Activate Virtual Environment

#### Windows
```bash
venv/Scripts/activate
```

#### Mac/Linux
```bash
source venv/bin/activate
```

#### Install Dependencies 
```bash
pip install -r requirements.txt
```

#### Run Performance Tests
```bash
python main/plot_performance_diff_graph_types.py
python main/plot_performance_diff_H_size.py
```

