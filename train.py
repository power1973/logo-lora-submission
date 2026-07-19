# train.py - 新版ms-swift兼容版
import os

cmd = """
swift sft \
    --model_type gemma \
    --model ./gemma-3-270m \
    --dataset ./train.jsonl \
    --val_dataset ./valid.jsonl \
    --lora_rank 8 \
    --lora_alpha 16 \
    --lora_dropout 0.1 \
    --output_dir ./adapter \
    --num_train_epochs 5 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --gradient_accumulation_steps 8 \
    --learning_rate 2e-4 \
    --warmup_ratio 0.05 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 50 \
    --eval_steps 50 \
    --save_total_limit 2 \
    --max_length 1024 \
    --max_new_tokens 512 \
    --optim adamw_torch \
    --weight_decay 0.01 \
    --seed 42 \
    --fp16 true \
    --bf16 false
"""

print("开始训练 Gemma-3-270M (新版兼容版)...")
print("注意: response_template/loss_only_response 在新版中已废弃，默认只计算响应部分损失")
os.system(cmd)
print("训练完成！")