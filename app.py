{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPu6axNOt+C1K4/kA9N8muc",
      "include_colab_link": True
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Cesaraville/Wine-Classifier/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "eFc7VdZsDtnN"
      },
      "outputs": [],
      "source": [
        "from flask import Flask, request, jsonify\n",
        "import joblib\n",
        "import numpy as np\n",
        "import os\n",
        "\n",
        "# Flask application instance\n",
        "app = Flask(__name__)  # This is the 'app' that Gunicorn is trying to find\n",
        "\n",
        "model = joblib.load('model.pkl')\n",
        "\n",
        "@app.route('/predict', methods=['POST'])\n",
        "def predict():\n",
        "    data = request.get_json()\n",
        "    features = np.array(data['features']).reshape(1, -1)\n",
        "    prediction = model.predict(features)\n",
        "    return jsonify({'prediction': prediction.tolist()})\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    # For local testing purposes\n",
        "    port = int(os.environ.get('PORT', 5000))\n",
        "    app.run(host='0.0.0.0', port=port)\n"
      ]
    }
  ]
}
