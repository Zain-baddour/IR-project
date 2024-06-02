import ir_datasets

from Evaluation.Docs import get_relevant_docs, get_retrieved_docs
from Evaluation.MeanAveragePrecision import get_mean_average_precision
from Evaluation.MeanReciprocalRank import get_mean_reciprocal_rank
from Evaluation.Precision import get_whole_precision, get_precision
from Evaluation.Recall import get_recall
from OffileOperations import create_corpus

name = "Q"
# calculate_recall(get_relevant_docs(q, name), get_retrieved_docs(q, name))
# get_precision("How patient a driver are you?","A")
# get_whole_precision(name)
# get_recall(name)
# get_mean_average_precision(name)
# get_mean_reciprocal_rank(name)

# antique_dataset = ir_datasets.load('antique')
# antique_test_dataset = ir_datasets.load('antique/test')
# antique_train_dataset = ir_datasets.load('antique/train')
# dataset_docs = antique_dataset.docs_iter()
# dataset_train = antique_train_dataset.docs_iter()
# create_corpus(dataset_docs, name)