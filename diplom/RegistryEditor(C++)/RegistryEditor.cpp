//Для создания/редактирования ключей реестра. Заполнение флагами.
#include <iostream>
#include <Windows.h>
#include <tchar.h>
#include <string>
#include <unordered_map>
#include <vector>

#define SIZE_REG_VALUE 100 
#define SIZE_REG_ARRAY 5 
#define MAINPATH _T("Software\\reg") 
#define REG_KEY1 _T("Key1")
#define REG_KEY2 _T("Key2")
#define REG_KEY3 _T("Key3")
#define REG_KEY4 _T("Key4")
#define REG_KEY5 _T("Key5")
#define REG_KEY6 _T("Key6")
#define REG_KEY7 _T("Key7")
#define REG_KEY8 _T("Key8")
#define REG_KEY9 _T("Key9")

class RegEdit
{
private:
    std::wstring myPath;
    HKEY hKey;

public:
    RegEdit(const std::wstring& path) : myPath(path), hKey(nullptr) {}

    bool OpenRegKey()
    {
        if (hKey != NULL)
            return false;
        LSTATUS status = RegOpenKeyEx(HKEY_CURRENT_USER, myPath.c_str(), 0, KEY_ALL_ACCESS, &hKey);
        return status == ERROR_SUCCESS;
    }

    bool CreateKey()
    {
        if (hKey != NULL)
            return false;
        DWORD dwValue = 0;
        LSTATUS status = RegCreateKeyEx(HKEY_CURRENT_USER, myPath.c_str(), 0, NULL, 0, KEY_ALL_ACCESS, NULL, &hKey, &dwValue);
        if (status != ERROR_SUCCESS)
        {
            return false;
        }
        std::cout << status << " Create" << std::endl;
        return true;
    }

    bool SetValue(const std::wstring& myKey, const std::wstring& data, DWORD sz)
    {
        if (hKey == NULL)
            return false;
        LSTATUS status = RegSetValueEx(hKey, myKey.c_str(), 0, REG_SZ, (BYTE*)data.c_str(), sz);
        std::cout << status << " Set" << std::endl;
        return false;
    }


    bool CloseKey()
    {
        if (hKey == NULL)
            return false;
        LSTATUS status = RegCloseKey(hKey);
        if (status == ERROR_SUCCESS)
        {
            hKey = NULL;
            return true;
        }
        return false;
    }

    bool GetRegKey()
    {
        DWORD regValueType = REG_SZ;
        DWORD valueSize = 0;
        LSTATUS status = RegQueryValueExW(hKey, TEXT("Key2"), NULL, &regValueType, NULL, &valueSize);
        if (status != ERROR_SUCCESS)
        {
            std::cout << status << std::endl;
            return false;
        }
        std::vector<BYTE> regTraceLevel(valueSize);
        status = RegQueryValueExW(hKey, TEXT("Key2"), NULL, &regValueType, regTraceLevel.data(), &valueSize);
        if (status != ERROR_SUCCESS)
        {
            std::cout << status << std::endl;
            return false;
        }
        std::wstring value = reinterpret_cast<std::wstring::value_type*>(regTraceLevel.data());
        std::wcout << value << std::endl;
        std::cout << status << std::endl;
        return true;

    }

    bool RegDelete()
    {
        LSTATUS status = RegDeleteKey(HKEY_CURRENT_USER, MAINPATH);
        if (status != ERROR_SUCCESS)
            return false;
        std::cout << " Весь раздел удален" << std::endl;
        return true;

    }

    ~RegEdit()
    {
        CloseKey();
    }

};

std::wstring GetFlag(const std::wstring& str, const std::wstring& select)
{
    std::wstring correctFlag;
    int result = str.find(TEXT('='));
    if (select == L"flag")
    {
        for (int i = 0; i < result; i++)
        {
            correctFlag += str[i];
        }
    }
    if (select == TEXT("value"))
    {
        for (size_t i = result + 1; i <= str.length(); i++)
        {
            correctFlag += str[i];
        }
    }
    return correctFlag;
}

int wmain(int argc, wchar_t *argv[])
{
    //////////////////////////
    SetConsoleOutputCP(65001);
    setlocale(LC_ALL, "RU");
    //////////////////////////
    std::wstring value;
    std::wstring correctFlag;
    std::wstring correctValue;
    DWORD sizeStr = 100;// todo почему 100?
    RegEdit reg(MAINPATH);
    std::wstring arrKeys[9]{REG_KEY1, REG_KEY2, REG_KEY3, REG_KEY4, REG_KEY5, REG_KEY6, REG_KEY7, REG_KEY8, REG_KEY9};
    std::unordered_map<std::wstring, std::wstring> regs;
    reg.OpenRegKey();
    for (int i = 1; i < argc; i++)
    {
        value = argv[i];
        correctFlag = GetFlag(value, TEXT("flag"));
        correctValue = GetFlag(value, TEXT("value"));
        regs.insert(std::make_pair(correctFlag, arrKeys[i-1]));
        auto iter = regs.find(correctFlag);
        if (iter != regs.end())
            reg.SetValue(iter->second, correctValue.c_str(), sizeStr);
        

    }

    return 0;
}