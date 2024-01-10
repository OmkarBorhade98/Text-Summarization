# Text Summarization Project

------- Project Work in Progress -------

### Create Conda Environment
```
conda env create -f environment.yml
```

### Model Information
- Dataset : [samsum](https://huggingface.co/datasets/samsum)
- Pre-Trained Tokenizer : [google/pegasus-cnn_dailymail](https://huggingface.co/google/pegasus-cnn_dailymail)
- Pre-Trained Model : [google/pegasus-cnn_dailymail](https://huggingface.co/google/pegasus-cnn_dailymail)

### Citation
```
@inproceedings{gliwa-etal-2019-samsum,
    title = "{SAMS}um Corpus: A Human-annotated Dialogue Dataset for Abstractive Summarization",
    author = "Gliwa, Bogdan  and
      Mochol, Iwona  and
      Biesek, Maciej  and
      Wawer, Aleksander",
    booktitle = "Proceedings of the 2nd Workshop on New Frontiers in Summarization",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D19-5409",
    doi = "10.18653/v1/D19-5409",
    pages = "70--79"
}
```

```
@misc{zhang2019pegasus,
    title={PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization},
    author={Jingqing Zhang and Yao Zhao and Mohammad Saleh and Peter J. Liu},
    year={2019},
    eprint={1912.08777},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```