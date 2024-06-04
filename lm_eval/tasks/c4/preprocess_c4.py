import re


def process_results(doc, results):
    (loglikelihood,) = results
    _words = len(re.split(r"\s+", doc["page"]))
    _bytes = len(doc["page"].encode("utf-8"))
    return {
        "word_perplexity": (loglikelihood, _words),
        "byte_perplexity": (loglikelihood, _bytes),
        "bits_per_byte": (loglikelihood, _bytes),
    }
