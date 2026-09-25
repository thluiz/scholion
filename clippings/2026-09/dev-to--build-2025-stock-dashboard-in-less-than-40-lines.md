---
url: "https://dev.to/taipy/build-a-stock-dashboard-in-less-than-40-lines-of-python-code-3b78?context=digest"
captured_at: "2026-09-25T01:08:03+01:00"
title: "Build a 2025 Stock Dashboard in less than 40 lines of Python code!🤓"
domain: "dev-to"
---

Building interactive data dashboards can seem intimidating.

Especially if you're unfamiliar with frontend technologies like HTML/CSS/ JS.

[![Lisan Al Gaib](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbhce6wjfxy357djxm3c3.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbhce6wjfxy357djxm3c3.png)

But what if you could create a fully functional, production-ready data science dashboard using just Python?

Enter [Taipy](https://github.com/Avaiga/taipy), an open-source library that simplifies the process of creating data apps.

[![Paul Atreides](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjk9rr9dv3qk9etxurr3b.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fjk9rr9dv3qk9etxurr3b.png)

[Star ⭐ Taipy repo](https://github.com/Avaiga/taipy)  
 

In this tutorial, Mariya Sha will guide you through building a stock value dashboard using [Taipy](https://github.com/Avaiga/taipy), [Plotly](https://plotly.com/), and a dataset from [Kaggle](https://www.kaggle.com/).

Our app will dynamically filter data, display graphs, and handle user inputs—all from scratch.

Ready to dive in? Let’s get started!

* * *

### [](#step-1-setting-up-your-environment)Step 1: Setting Up Your Environment

First, we need to create a new Python environment. If you use Conda, you can set it up as follows:  

```
conda create -n ds_env python=3.11
conda activate ds_env
pip install taipy pandas plotly

```

Enter fullscreen mode Exit fullscreen mode

Clone the resources for this project:  

```
git clone https://github.com/MariyaSha/data_science_dashboard.git
cd data_science_dashboard/starter_files

```

Enter fullscreen mode Exit fullscreen mode

This will serve as our project root directory. Inside, you’ll find images, a wireframe, and a Python file (`main.py`) to start.

* * *

### [](#step-2-designing-the-gui-with-taipy)Step 2: Designing the GUI with Taipy

Let’s add a header and a logo to our app. Open main.py and start coding:  

```
import taipy.gui as tgb

with tgb.page("Stock Dashboard"):
    # Add a logo
    tgb.image("images/icons/logo.png", width="10vw")

    # Add a title
    tgb.text("# S&P 500 Stock Value Over Time", mode="md")

```

Enter fullscreen mode Exit fullscreen mode

Run your app:  

```
taipy run main.py
```

Enter fullscreen mode Exit fullscreen mode

Navigate to [http://localhost:5000](http://localhost:5000/), and you’ll see your basic app!

* * *

### [](#step-3-adding-user-inputs)Step 3: Adding User Inputs

To filter data by date, add a date range selector:  

```
import datetime

dates = [datetime.date(2023, 1, 1), datetime.date(2024, 1, 1)]

with tgb.page("Stock Dashboard"):
    # Existing elements...

    # Add date range selector
    tgb.date_range(
        value="{dates}",
        label_start="Start Date",
        label_end="End Date",
    )

```

Enter fullscreen mode Exit fullscreen mode

* * *

### [](#step-4-dynamic-data-handling-with-taipy)Step 4: Dynamic Data Handling with Taipy

Let’s load our dataset and filter it dynamically based on user inputs.  

```
import pandas as pd

# Load the stock data
stock_data = pd.read_csv("data/sp500_stocks.csv")

def filter_data(state, name, value):
    if name == "dates":
        start, end = state.dates
        filtered_data = stock_data[
            (stock_data["Date"] >= str(start)) & 
            (stock_data["Date"] <= str(end))
        ]
        state.filtered_data = filtered_data

tgb.add_callback("filter_data", filter_data)

```

Enter fullscreen mode Exit fullscreen mode

* * *

### [](#step-5-visualizing-the-data)Step 5: Visualizing the Data

Finally, let’s plot the data with Plotly:  

```
import plotly.graph_objects as go

def create_chart(data):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=data["Date"],
            y=data["High"],
            name="Stock Value",
            mode="lines"
        )
    )
    return fig

with tgb.page("Stock Dashboard"):
    # Existing elements...

    # Display the chart
    tgb.chart(figure="{create_chart(filtered_data)}")

```

Enter fullscreen mode Exit fullscreen mode

* * *

### [](#final-thoughts)Final Thoughts

And voilà!  
You’ve built a stock dashboard with [Taipy](https://github.com/Avaiga/taipy), handling dynamic user inputs and data visualization—all without writing a single line of HTML, CSS, or JavaScript.

**Want to take it further?**

Explore Taipy Scenarios to enable even more dynamic backend interactions. Check out the official [Taipy GitHub repository](https://github.com/Avaiga/taipy) and contribute to their open-source initiatives!

* * *

PS: you can watch the video tutorial [here](https://www.youtube.com/watch?v=hxYIpH94u20&feature=youtu.be).
