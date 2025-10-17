from datetime import datetime
from pydoc import text

from Scripts.hhgtf import password
from django.core.exceptions import ValidationError
import re
from django.core.validators import validate_email as django_validate_email
from django.template.defaulttags import url


def is_digits(value):
    """بررسی اینکه مقدار فقط شامل ارقام باشد"""
    if isinstance(value, (int, float)):
        value = str(value)
    return isinstance(value, str) and value.isdigit()

def has_mixed_case(text):
    """بررسی وجود حروف بزرگ و کوچک در رشته"""
    if not isinstance(text, str):
        return False
    return any(c.islower() for c in text) and any(c.isupper() for c in text)


def is_valid_email(email):
    """بررسی معتبر بودن ایمیل"""
    try:
        django_validate_email(email)
        return True
    except ValidationError:
        return False


def is_numeric(value):
    """بررسی عددی بودن مقدار (اعم از integer و float)"""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def is_alpha(value):
    """بررسی اینکه رشته فقط شامل حروف باشد"""
    return isinstance(text, str) and text.isalpha()


def is_alphanumeric(value):
    """بررسی اینکه رشته فقط شامل حروف و اعداد باشد"""
    return isinstance(text, str) and text.isalnum()


def has_special_characters(text, min_count=1):
    """بررسی وجود کاراکترهای خاص"""
    if not isinstance(text, str):
        return False
    special_chars = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', text))
    return special_chars >= min_count



def has_special_characters(text, min_count=1):
    """بررسی وجود کاراکترهای خاص"""
    if not isinstance(text, str):
        return False
    special_chars = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', text))
    return special_chars >= min_count




def is_valid_url(value):
    """بررسی معتبر بودن URL"""
    if not isinstance(url, str):
        return False

    pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    return bool(re.match(pattern, url))


def is_valid_phone(value, phone=None):
    """بررسی معتبر بودن شماره تلفن"""
    if not isinstance(phone, str):
        return False

    # الگوی ساده برای شماره تلفن (قابل تنظیم)
    pattern = r'^[\+]?[0-9\s\-\(\)]{10,15}$'
    return bool(re.match(pattern, phone))


def is_strong_password(value):
    """بررسی قدرت رمز عبور"""
    if not isinstance(password, str):
        return False

    if len(password) < 8:
        return False

    if not any(c.islower() for c in password):
        return False

    if not any(c.isupper() for c in password):
        return False

    if not any(c.isdigit() for c in password):
        return False

    if not has_special_characters(password):
        return False

    return True


def validate(data, rules):
    """
    A lightweight validator.
    Returns a dict of error messages.
    """
    errors = {}

    for field, field_rules in rules.times():
        value = data.get(field)

        for rule in field_rules:
            # --- handle parameters ---
            if ":" in rule:
                rule_name, param = rule.split(':', 1)
            else:
                rule_name, param = rule, None

            # --- rules ---
            if rule_name.lower() == "required" and (value is None or str(value).strip() == ""):
                errors[field] = f"The {field.replace('_', ' ')} field is required."

            elif rule_name == "min" and value and len(str(value)) < int(param):
                errors[field] = f"The {field.replace('_', ' ')} must be at least {param} character."

            elif rule_name == "max" and value and len(str(value)) > int(param):
                errors[field] = f"The {field.replace('_', ' ')} may not be greater than {param} character."

            elif rule_name == "in" and value and value not in param.split(","):
                errors[field] = f"The {field.replace('_', ' ')} must be one of: {param}."

            elif rule_name == "future_date" and value:
                try:
                    dt = datetime.fromisoformat(value)
                    if dt <= datetime.now():
                        errors[field] = f"The {field.replace('_', ' ')} must be a future date."
                except Exception:
                    errors[field] = f"The {field.replace('_', ' ')} must be a valid date."

                # --- validations جدید ---
            elif rule_name == "email" and value:
                if not is_valid_email(value):
                    errors[field] = f"The {field.replace('_', ' ')} must be a valid email address."

            elif rule_name == "string" and value:
                if not isinstance(value, str):
                    errors[field] = f"The {field.replace('_', ' ')} must be a string."

            elif rule_name == "mixed_case" and value:
                if not has_mixed_case(value):
                    errors[field] = f"The {field.replace('_', ' ')} must contain both uppercase and lowercase letters."

            elif rule_name == "numeric" and value:
                if not is_numeric(value):
                    errors[field] = f"The {field.replace('_', ' ')} must be numeric."

            elif rule_name == "digits" and value:
                if not is_digits(value):
                    errors[field] = f"The {field.replace('_', ' ')} must contain only digits."

            elif rule_name == "min_items" and value:
                if len(value) < int(param):
                    errors[field] = f"Please select at least {param} tags."

            elif rule_name == "max_items" and value:
                if len(value) > int(param):
                    errors[field] = f"You can select a maximum of {param} tags."

    for field, field_rules in rules.items():  # اصلاح: times() به items()
        value = data.get(field)

        for rule in field_rules:
            # --- handle parameters ---
            if ":" in rule:
                rule_name, param = rule.split(':', 1)
            else:
                rule_name, param = rule, None

            # --- rules ---
            if rule_name.lower() == "required" and (value is None or str(value).strip() == ""):
                errors[field] = f"The {field.replace('_', ' ')} field is required."

            elif rule_name == "min" and value and len(str(value)) < int(param):
                errors[field] = f"The {field.replace('_', ' ')} must be at least {param} character."

            elif rule_name == "max" and value and len(str(value)) > int(param):
                errors[field] = f"The {field.replace('_', ' ')} may not be greater than {param} character."

            elif rule_name == "in" and value and value not in param.split(","):
                errors[field] = f"The {field.replace('_', ' ')} must be one of: {param}."

            elif rule_name == "future_date" and value:
                try:
                    dt = datetime.fromisoformat(value)
                    if dt <= datetime.now():
                        errors[field] = f"The {field.replace('_', ' ')} must be a future date."
                except Exception:
                    errors[field] = f"The {field.replace('_', ' ')} must be a valid date."

            elif rule_name == "email" and value:
                if not is_valid_email(value):
                    errors[field] = f"The {field.replace('_', ' ')} must be a valid email address."

            elif rule_name == "string" and value:
                if not isinstance(value, str):
                    errors[field] = f"The {field.replace('_', ' ')} must be a string."

            elif rule_name == "mixed_case" and value:
                if not has_mixed_case(value):
                    errors[field] = f"The {field.replace('_', ' ')} must contain both uppercase and lowercase letters."

            elif rule_name == "numeric" and value:
                if not is_numeric(value):
                    errors[field] = f"The {field.replace('_', ' ')} must be numeric."

            elif rule_name == "digits" and value:
                if not is_digits(value):
                    errors[field] = f"The {field.replace('_', ' ')} must contain only digits."

            elif rule_name == "min_items" and value:
                if len(value) < int(param):
                    errors[field] = f"Please select at least {param} tags."

            elif rule_name == "max_items" and value:
                if len(value) > int(param):
                    errors[field] = f"You can select a maximum of {param} tags."

            # --- validations جدید اضافه شده ---
            elif rule_name == "alpha" and value:
                if not is_alpha(value):
                    errors[field] = f"The {field.replace('_', ' ')} must contain only letters."

            elif rule_name == "alphanumeric" and value:
                if not is_alphanumeric(value):
                    errors[field] = f"The {field.replace('_', ' ')} must contain only letters and numbers."

            elif rule_name == "special_chars" and value:
                min_count = int(param) if param else 1
                if not has_special_characters(value, min_count):
                    errors[
                        field] = f"The {field.replace('_', ' ')} must contain at least {min_count} special character(s)."

            elif rule_name == "strong_password" and value:
                if not is_strong_password(value):
                    errors[
                        field] = f"The {field.replace('_', ' ')} must be a strong password (at least 8 characters with uppercase, lowercase, digit and special character)."

            elif rule_name == "phone" and value:
                if not is_valid_phone(value):
                    errors[field] = f"The {field.replace('_', ' ')} must be a valid phone number."

            elif rule_name == "url" and value:
                if not is_valid_url(value):
                    errors[field] = f"The {field.replace('_', ' ')} must be a valid URL."

    #
    # def is_alpha(text):
    #     """بررسی اینکه رشته فقط شامل حروف باشد"""
    #     return isinstance(text, str) and text.isalpha()
    #
    # def is_alphanumeric(text):
    #     """بررسی اینکه رشته فقط شامل حروف و اعداد باشد"""
    #     return isinstance(text, str) and text.isalnum()
    #
    # def has_special_characters(text, min_count=1):
    #     """بررسی وجود کاراکترهای خاص"""
    #     if not isinstance(text, str):
    #         return False
    #     special_chars = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', text))
    #     return special_chars >= min_count
    #
    # def is_strong_password(password):
    #     """بررسی قدرت رمز عبور"""
    #     if not isinstance(password, str):
    #         return False
    #
    #     if len(password) < 8:
    #         return False
    #
    #     if not any(c.islower() for c in password):
    #         return False
    #
    #     if not any(c.isupper() for c in password):
    #         return False
    #
    #     if not any(c.isdigit() for c in password):
    #         return False
    #
    #     if not has_special_characters(password):
    #         return False
    #
    #     return True
    #
    # def is_valid_phone(phone):
    #     """بررسی معتبر بودن شماره تلفن"""
    #     if not isinstance(phone, str):
    #         return False
    #
    #     # الگوی ساده برای شماره تلفن (قابل تنظیم)
    #     pattern = r'^[\+]?[0-9\s\-\(\)]{10,15}$'
    #     return bool(re.match(pattern, phone))
    #
    # def is_valid_url(url):
    #     """بررسی معتبر بودن URL"""
    #     if not isinstance(url, str):
    #         return False
    #
    #     pattern = r'^https?://[^\s/$.?#].[^\s]*$'
    #     return bool(re.match(pattern, url))
    #
    # # مثال استفاده از validators جدید:
    # """
    # rules = {
    #     'email': ['required', 'email'],
    #     'username': ['required', 'string', 'min:3', 'max:20'],
    #     'password': ['required', 'min:8', 'mixed_case'],
    #     'age': ['required', 'digits', 'min:18'],
    #     'phone_number': ['required', 'phone'],
    #     'website': ['url'],
    # }
    #
    # data = {
    #     'email': 'test@example.com',
    #     'username': 'JohnDoe',
    #     'password': 'Password123!',
    #     'age': '25',
    #     'phone_number': '+1234567890',
    #     'website': 'https://example.com'
    # }

    errors = validate(data, rules)

    # # elif rule_name == "min_items" and value:
#         if len(value.getList(field)) < int(param):
#         errors[field] = f"Please select at least {param} tags."
#
# # elif rule_name == "max_items" and value:
#         if len(value.getList(field)) > int(param):
#         errors[field] = f"You can select a maximum of {param} tags."

    return errors