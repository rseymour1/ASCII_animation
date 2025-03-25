"""Converts the clip output table into a meaningful loss function"""

def create_loss_function(label_list: list, prob_list: list, true_label: str):
    """creates a loss function from the output of open_clip
    Input:
        label_list {list} -- list of labels
        prob_list {list} -- list of probabilities for each of the labels
        true_label {str} -- the true label for the ASCII art
    Returns:
        ...
    """
    