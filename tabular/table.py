import torch
torch.__version__
from transformers import TapasTokenizer, TapasForQuestionAnswering
from transformers import TrainingArguments, Trainer
from transformers import pipeline
import pandas as pd
from datasets import load_dataset
from sklearn.metrics import accuracy_score

def output_table(file,question):
    dataset_name = 'inria-soda/tabular-benchmark'
    config_name = 'clf_cat_road-safety'
    dataset = load_dataset(dataset_name, config_name, split="train")
    type(dataset)

    df = pd.DataFrame(dataset)
    df.fillna('', inplace=True)
    df.reset_index(drop=True, inplace=True)
    df = df.astype(str)


    # train the model
    tqa = pipeline(task="table-question-answering",
                model="google/tapas-base-finetuned-wtq")

    # Initialize the tokenizer and model
    model_name = "google/tapas-base-finetuned-wtq"
    tokenizer = TapasTokenizer.from_pretrained(model_name)
    model = TapasForQuestionAnswering.from_pretrained(model_name)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=1000,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=64,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=df,
    )

    # df.iloc[47076:]
    df.index

    try:
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=df,
        )
        trainer.train()
    except KeyError as e:
        print("KeyError encountered:", e)

    table = pd.read_excel(file)
    table = table.astype(str)

    table

    """**Questions for answering**"""

    # query = "Who has scored the highest runs?"
    answer = tqa(table=table, query=question)["answer"]

    # Now you can print 'answer'
    print(answer)

    # """**Accuracy**"""

    # # Example evaluation dataset
    # eval_data = [
    #     {"table": table, "question": "Who has scored the highest runs?", "answer": "Sachin Tendulkar"},
    #     {"table": table, "question": "Virat Kohli's highest score?", "answer": "183"}
    #     # Add more question-answer-table tuples
    # ]

    # # Generate predictions
    # true_answers = [item["answer"] for item in eval_data]
    # predicted_answers = []

    # for item in eval_data:
    #     inputs = tokenizer(table=item["table"], queries=item["question"], padding='max_length', return_tensors="pt")
    #     outputs = model(**inputs)
    #     predicted_answer = tokenizer.decode(outputs.logits.argmax(dim=-1)[0]).strip()
    #     predicted_answers.append(predicted_answer)

    # # Calculate accuracy
    # accuracy = accuracy_score(true_answers, predicted_answers)
    # print("Model Accuracy:", accuracy)

    return answer