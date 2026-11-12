# Store Planning Dashboard (Cloud Run + BigQuery)

## Deploy
1. เปิด Cloud Shell ในโปรเจกต์ datastory-analytic-mis แล้วอัปโหลดโฟลเดอร์นี้
2. สั่ง:
   gcloud run deploy store-dashboard --source . --region asia-southeast1 --allow-unauthenticated
   (ถ้าเป็นข้อมูลภายใน แนะนำเอา --allow-unauthenticated ออก แล้วใช้ IAM / IAP จำกัดผู้ใช้)
3. ให้สิทธิ์ Service Account ของ Cloud Run (ดูได้ในหน้า service > Security):
   - BigQuery Job User (ระดับโปรเจกต์)
   - BigQuery Data Viewer (ระดับ dataset pop_coverage_poc)
4. เปิด URL ที่ได้

## ทดสอบในเครื่อง
   gcloud auth application-default login
   pip install -r requirements.txt && python main.py
   เปิด http://localhost:8080

เปลี่ยนตารางได้ด้วย env var BQ_TABLE
