# Lộ trình DSA → ML → DL trong 3 tháng (12 tuần)

> Dành cho người đã biết C++. Giả định học **3 đến 4 giờ/ngày**, 6 ngày/tuần (nghỉ 1 ngày).
> 3 tháng là lịch **rất nén**: mục tiêu là nắm nền tảng và làm được project, không phải thành thạo hoàn toàn. Nếu ít thời gian hơn, kéo dài mỗi tháng thành 1,5 tháng.

---

## Nguyên tắc chung

- **Chia thời gian mỗi ngày:** ~1 giờ DSA (luôn duy trì) + ~2 đến 3 giờ cho chủ đề chính của tháng.
- **Học bằng cách làm:** mỗi kiến thức mới phải có code chạy được ngay.
- **Không học hết toán rồi mới học ML.** Gặp chỗ nào chưa hiểu thì quay lại bổ sung.
- **Mỗi tháng 1 project** để kiểm chứng kiến thức.
- Ghi chú ngắn mỗi ngày (học gì, vướng gì) vào một file riêng.

---

## Tài nguyên chính (chỉ dùng bấy nhiêu, tránh sa đà)

| Mảng | Tài nguyên |
|---|---|
| Python | https://www.w3schools.com/python/ , Python Tutorial chính thức |
| DSA | NeetCode Roadmap (neetcode.io), LeetCode |
| Toán | 3Blue1Brown (Linear Algebra, Calculus), StatQuest |
| ML | Machine Learning Specialization (Andrew Ng, Coursera), scikit-learn docs, Kaggle |
| DL | Karpathy "Neural Networks: Zero to Hero", PyTorch tutorials, fast.ai |

---

## THÁNG 1: Python + DSA + Nền tảng dữ liệu (Tuần 1 đến 4)

**Mục tiêu:** viết Python thành thạo, nắm các cấu trúc dữ liệu và thuật toán cốt lõi, quen NumPy/Pandas.

### Tuần 1: Python cơ bản + NumPy
- [ ] W3Schools Python: Variables, Data Types, Strings, Lists, Tuples, Sets, Dicts
- [ ] If/Else, Loops, Functions, Lambda, Classes, Modules, File Handling, Try/Except
- [ ] List comprehension, slicing, mutable vs immutable
- [ ] NumPy: array, indexing, broadcasting, các phép toán ma trận
- [ ] DSA: làm lại 10 bài Easy bằng Python (Arrays & Hashing)

### Tuần 2: DSA phần 1
- [ ] Độ phức tạp thuật toán (Big-O)
- [ ] Arrays & Hashing, Two Pointers, Sliding Window
- [ ] Stack, Queue
- [ ] Mục tiêu: **15 đến 20 bài** LeetCode (Easy + một ít Medium)

### Tuần 3: DSA phần 2
- [ ] Binary Search, Linked List
- [ ] Trees (BST, duyệt DFS/BFS), Heap / Priority Queue
- [ ] Đệ quy, Backtracking cơ bản
- [ ] Mục tiêu: **15 đến 20 bài**
- [ ] Học thêm: Pandas cơ bản (DataFrame, đọc CSV, lọc, groupby), Matplotlib

### Tuần 4: DSA phần 3 + Toán nền
- [ ] Graphs (BFS, DFS, topological sort, Dijkstra cơ bản)
- [ ] Dynamic Programming cơ bản (1D, knapsack, LCS)
- [ ] Sắp xếp (quick, merge) và hiểu độ phức tạp
- [ ] Mục tiêu: **15 bài**, tổng tháng 1 khoảng **60 đến 70 bài**
- [ ] Xem 3Blue1Brown "Essence of Linear Algebra" (vector, ma trận, nhân ma trận)

### Project tháng 1
Phân tích một dataset nhỏ (ví dụ Titanic) bằng Pandas + Matplotlib: làm sạch dữ liệu, vẽ biểu đồ, rút ra nhận xét.

---

## THÁNG 2: Machine Learning (Tuần 5 đến 8)

**Mục tiêu:** hiểu và tự cài đặt các thuật toán ML cơ bản, dùng thành thạo scikit-learn.

### Tuần 5: Hồi quy
- [ ] Andrew Ng ML Specialization, Course 1: Linear Regression, Gradient Descent
- [ ] 3Blue1Brown "Essence of Calculus" (đạo hàm, chain rule)
- [ ] **Tự cài đặt** linear regression + gradient descent bằng NumPy
- [ ] DSA: 1 bài/ngày (ôn lại các chủ đề yếu)

### Tuần 6: Phân loại
- [ ] Logistic Regression, overfitting/underfitting, regularization
- [ ] Train/validation/test, cross-validation
- [ ] Metrics: accuracy, precision, recall, F1, ROC-AUC
- [ ] StatQuest: xác suất, phân phối, bias-variance

### Tuần 7: Các mô hình ML cổ điển
- [ ] Decision Tree, Random Forest, Gradient Boosting (XGBoost)
- [ ] KNN, SVM (hiểu ý tưởng chính)
- [ ] K-Means, PCA
- [ ] Thực hành với **scikit-learn**

### Tuần 8: Thực hành và đúc kết
- [ ] Hoàn thành Course 2 của ML Specialization (Neural Networks cơ bản) nếu còn thời gian
- [ ] Feature engineering, xử lý dữ liệu thiếu, pipeline
- [ ] Làm 1 cuộc thi Kaggle cho người mới (House Prices hoặc Titanic)

### Project tháng 2
Giải bài toán Kaggle hoàn chỉnh: EDA → feature engineering → thử nhiều mô hình → so sánh bằng cross-validation → viết báo cáo ngắn.

---

## THÁNG 3: Deep Learning (Tuần 9 đến 12)

**Mục tiêu:** hiểu cách mạng nơ-ron hoạt động bên trong, dùng PyTorch để huấn luyện mô hình thực tế.

### Tuần 9: Nền tảng neural network
- [ ] Karpathy "Zero to Hero": video **micrograd** (tự cài đặt backprop)
- [ ] Perceptron, hàm kích hoạt, forward/backward pass
- [ ] PyTorch: tensor, autograd, `nn.Module`, vòng lặp huấn luyện

### Tuần 10: Huấn luyện mạng và CNN
- [ ] Optimizer (SGD, Adam), learning rate, batch norm, dropout
- [ ] Karpathy: makemore (language model đơn giản)
- [ ] CNN: convolution, pooling; huấn luyện trên MNIST/CIFAR-10

### Tuần 11: Sequence và Transformer
- [ ] RNN/LSTM (hiểu khái niệm)
- [ ] Attention và Transformer (Karpathy "Let's build GPT" hoặc The Illustrated Transformer)
- [ ] Làm quen Hugging Face: dùng mô hình pretrained, fine-tune nhỏ

### Tuần 12: Project cuối + ôn tập
- [ ] Hoàn thành project cuối (xem bên dưới)
- [ ] Đưa code lên **GitHub**, viết README rõ ràng
- [ ] Ôn lại DSA: làm lại các bài đã sai, mock interview nếu cần

### Project tháng 3 (chọn 1)
- Phân loại ảnh bằng CNN (transfer learning với ResNet) trên dataset tự chọn
- Phân loại văn bản/cảm xúc bằng mô hình pretrained từ Hugging Face
- Chatbot hoặc tóm tắt văn bản tiếng Việt đơn giản

---

## Bảng theo dõi tiến độ

| Tuần | Chủ đề chính | Số bài DSA | Hoàn thành |
|---|---|---|---|
| 1 | Python, NumPy | 10 | [ ] |
| 2 | Arrays, Two Pointers, Stack | 15 đến 20 | [ ] |
| 3 | Binary Search, Linked List, Tree | 15 đến 20 | [ ] |
| 4 | Graph, DP | 15 | [ ] |
| 5 | Linear Regression | 5 | [ ] |
| 6 | Logistic Regression, Metrics | 5 | [ ] |
| 7 | Tree models, Clustering | 5 | [ ] |
| 8 | Kaggle project | 5 | [ ] |
| 9 | Backprop, PyTorch | 5 | [ ] |
| 10 | CNN | 5 | [ ] |
| 11 | Transformer | 5 | [ ] |
| 12 | Project cuối | ôn tập | [ ] |

---

## Lời khuyên để không bị hụt hơi

1. **Đều mỗi ngày quan trọng hơn học dồn.** Lỡ một ngày thì học bù nhẹ, đừng bỏ cả tuần.
2. **Kẹt một bài DSA quá 30 đến 45 phút thì xem lời giải**, hiểu rồi tự code lại ngày hôm sau.
3. **Đừng sa đà vào quá nhiều khóa học.** Chọn đúng tài nguyên ở bảng trên và học đến nơi đến chốn.
4. **Tự cài đặt ít nhất một lần** các thuật toán cốt lõi (linear regression, logistic regression, backprop) trước khi dùng thư viện.
5. **Sau 3 tháng**, hướng đi tiếp theo: luyện DSA sâu hơn (200 bài trở lên), học MLOps cơ bản, đọc paper, hoặc làm project gắn với lĩnh vực bạn quan tâm.
