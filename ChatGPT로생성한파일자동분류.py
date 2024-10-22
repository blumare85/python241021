import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 파일을 이동할 대상 폴더 경로
folders = {
    'images': ['.jpg', '.jpeg'],
    'data': ['.csv', '.xlsx'],
    'docs': ['.txt', '.doc', '.pdf'],
    'archive': ['.zip']
}

# 폴더 생성 함수
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 파일 이동 함수
def move_files():
    # 각 파일 확장자에 맞는 폴더 경로 설정
    for folder, extensions in folders.items():
        target_folder = os.path.join(download_folder, folder)
        create_folder_if_not_exists(target_folder)  # 폴더가 없으면 생성

        # 다운로드 폴더의 모든 파일을 확인
        for file_name in os.listdir(download_folder):
            file_path = os.path.join(download_folder, file_name)
            
            # 파일일 경우에만 처리
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(file_name)[1].lower()  # 파일 확장자 추출
                
                # 파일 확장자가 해당하는 경우 폴더로 이동
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(target_folder, file_name))
                    print(f"Moved {file_name} to {target_folder}")

# 파일 이동 실행
if __name__ == "__main__":
    move_files()
