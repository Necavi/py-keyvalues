import sys
sys.path.append("..")
import keyvalues

kv = keyvalues.keyvalues()
kv.load_from_file("databases.cfg")
kv.kv["Databases"]["driver_default"] = "mysql"
kv.recurse_keyvalues()
kv.save_to_file("databases_changed.cfg")
