from vox_bridge.utils.argostranslate import package, translate

from_code = "hi"
to_code = "en"

package.update_package_index()
available_packages = package.get_available_packages()
package_to_install = next(
    filter(
        lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
    )
)
package.install_from_path(package_to_install.download())
def translate_text(hi_text, en_text):
    hi_content= ""
    with open(hi_text, "r", encoding="utf-8") as file:
        hi_content = file.read()
    en_content = translate.translate(hi_content, from_code, to_code)
    with open(en_text, "w", encoding="utf-8") as file:
        file.write(en_content)