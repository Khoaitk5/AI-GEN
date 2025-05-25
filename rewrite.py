from labels import LABELS

def binarize_labels_fixed(input_csv, output_csv):
    labels_list = LABELS  # thứ tự nhãn cố định
    
    lines = []
    with open(input_csv, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            sample, labels_str = line.split(":", 1)
            labels = [l.strip() for l in labels_str.split(",") if l.strip()]
            lines.append((sample.strip(), labels))
    
    with open(output_csv, 'w', encoding='utf-8') as f_out:
        # Viết header
        header = ["filename"] + labels_list
        f_out.write(",".join(header) + "\n")
        
        # Viết từng dòng dữ liệu
        for sample, labels in lines:
            vector = ['1' if label in labels else '0' for label in labels_list]
            vector_str = ",".join(vector)
            f_out.write(f"{sample},{vector_str}\n")
    
    print(f"[DONE] Processed {len(lines)} samples with {len(labels_list)} fixed labels.")


# Gọi hàm
binarize_labels_fixed("module/pre_dataset.csv", "module/pro_dataset.csv")
