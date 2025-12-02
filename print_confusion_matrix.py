def print_confusion_matrix(cm, print_metrics=False):
    tn, fp, fn, tp = cm.ravel()
    # Header
    print(f"{'':>14}{'Predicted':^8}")
    print(f"{'':>14}{'fail':>4} {'pass':>4}")
    print("-" * 24)
    # Rows
    print(f"{'Actual: fail':>14}{tn:>4} {fp:>4}")
    print(f"{'Actual: pass':>14}{fn:>4} {tp:>4}")
    print("-" * 24)

    if print_metrics:
        total = tn + fp + fn + tp
        accuracy = (tn + tp) / total if total else 0
        recall = tp / (tp + fn) if (tp + fn) else 0
        precision = tp / (tp + fp) if (tp + fp) else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) else 0

        print(f"Accuracy : {accuracy:6.3f}")
        print(f"Precision: {precision:6.3f}")
        print(f"Recall   : {recall:6.3f}")
        print(f"F1-score : {f1_score:6.3f}\n")