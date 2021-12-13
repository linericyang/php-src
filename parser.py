#!/usr/bin/env python3
import json
import sys


OPCODES = [
    "ZEND_NOP",
    "ZEND_ADD",
    "ZEND_SUB",
    "ZEND_MUL",
    "ZEND_DIV",
    "ZEND_MOD",
    "ZEND_SL",
    "ZEND_SR",
    "ZEND_CONCAT",
    "ZEND_BW_OR",
    "ZEND_BW_AND",
    "ZEND_BW_XOR",
    "ZEND_POW",
    "ZEND_BW_NOT",
    "ZEND_BOOL_NOT",
    "ZEND_BOOL_XOR",
    "ZEND_IS_IDENTICAL",
    "ZEND_IS_NOT_IDENTICAL",
    "ZEND_IS_EQUAL",
    "ZEND_IS_NOT_EQUAL",
    "ZEND_IS_SMALLER",
    "ZEND_IS_SMALLER_OR_EQUAL",
    "ZEND_ASSIGN",
    "ZEND_ASSIGN_DIM",
    "ZEND_ASSIGN_OBJ",
    "ZEND_ASSIGN_STATIC_PROP",
    "ZEND_ASSIGN_OP",
    "ZEND_ASSIGN_DIM_OP",
    "ZEND_ASSIGN_OBJ_OP",
    "ZEND_ASSIGN_STATIC_PROP_OP",
    "ZEND_ASSIGN_REF",
    "ZEND_QM_ASSIGN",
    "ZEND_ASSIGN_OBJ_REF",
    "ZEND_ASSIGN_STATIC_PROP_REF",
    "ZEND_PRE_INC",
    "ZEND_PRE_DEC",
    "ZEND_POST_INC",
    "ZEND_POST_DEC",
    "ZEND_PRE_INC_STATIC_PROP",
    "ZEND_PRE_DEC_STATIC_PROP",
    "ZEND_POST_INC_STATIC_PROP",
    "ZEND_POST_DEC_STATIC_PROP",
    "ZEND_JMP",
    "ZEND_JMPZ",
    "ZEND_JMPNZ",
    "ZEND_JMPZNZ",
    "ZEND_JMPZ_EX",
    "ZEND_JMPNZ_EX",
    "ZEND_CASE",
    "ZEND_CHECK_VAR",
    "ZEND_SEND_VAR_NO_REF_EX",
    "ZEND_CAST",
    "ZEND_BOOL",
    "ZEND_FAST_CONCAT",
    "ZEND_ROPE_INIT",
    "ZEND_ROPE_ADD",
    "ZEND_ROPE_END",
    "ZEND_BEGIN_SILENCE",
    "ZEND_END_SILENCE",
    "ZEND_INIT_FCALL_BY_NAME",
    "ZEND_DO_FCALL",
    "ZEND_INIT_FCALL",
    "ZEND_RETURN",
    "ZEND_RECV",
    "ZEND_RECV_INIT",
    "ZEND_SEND_VAL",
    "ZEND_SEND_VAR_EX",
    "ZEND_SEND_REF",
    "ZEND_NEW",
    "ZEND_INIT_NS_FCALL_BY_NAME",
    "ZEND_FREE",
    "ZEND_INIT_ARRAY",
    "ZEND_ADD_ARRAY_ELEMENT",
    "ZEND_INCLUDE_OR_EVAL",
    "ZEND_UNSET_VAR",
    "ZEND_UNSET_DIM",
    "ZEND_UNSET_OBJ",
    "ZEND_FE_RESET_R",
    "ZEND_FE_FETCH_R",
    "ZEND_EXIT",
    "ZEND_FETCH_R",
    "ZEND_FETCH_DIM_R",
    "ZEND_FETCH_OBJ_R",
    "ZEND_FETCH_W",
    "ZEND_FETCH_DIM_W",
    "ZEND_FETCH_OBJ_W",
    "ZEND_FETCH_RW",
    "ZEND_FETCH_DIM_RW",
    "ZEND_FETCH_OBJ_RW",
    "ZEND_FETCH_IS",
    "ZEND_FETCH_DIM_IS",
    "ZEND_FETCH_OBJ_IS",
    "ZEND_FETCH_FUNC_ARG",
    "ZEND_FETCH_DIM_FUNC_ARG",
    "ZEND_FETCH_OBJ_FUNC_ARG",
    "ZEND_FETCH_UNSET",
    "ZEND_FETCH_DIM_UNSET",
    "ZEND_FETCH_OBJ_UNSET",
    "ZEND_FETCH_LIST_R",
    "ZEND_FETCH_CONSTANT",
    "ZEND_CHECK_FUNC_ARG",
    "ZEND_EXT_STMT",
    "ZEND_EXT_FCALL_BEGIN",
    "ZEND_EXT_FCALL_END",
    "ZEND_EXT_NOP",
    "ZEND_TICKS",
    "ZEND_SEND_VAR_NO_REF",
    "ZEND_CATCH",
    "ZEND_THROW",
    "ZEND_FETCH_CLASS",
    "ZEND_CLONE",
    "ZEND_RETURN_BY_REF",
    "ZEND_INIT_METHOD_CALL",
    "ZEND_INIT_STATIC_METHOD_CALL",
    "ZEND_ISSET_ISEMPTY_VAR",
    "ZEND_ISSET_ISEMPTY_DIM_OBJ",
    "ZEND_SEND_VAL_EX",
    "ZEND_SEND_VAR",
    "ZEND_INIT_USER_CALL",
    "ZEND_SEND_ARRAY",
    "ZEND_SEND_USER",
    "ZEND_STRLEN",
    "ZEND_DEFINED",
    "ZEND_TYPE_CHECK",
    "ZEND_VERIFY_RETURN_TYPE",
    "ZEND_FE_RESET_RW",
    "ZEND_FE_FETCH_RW",
    "ZEND_FE_FREE",
    "ZEND_INIT_DYNAMIC_CALL",
    "ZEND_DO_ICALL",
    "ZEND_DO_UCALL",
    "ZEND_DO_FCALL_BY_NAME",
    "ZEND_PRE_INC_OBJ",
    "ZEND_PRE_DEC_OBJ",
    "ZEND_POST_INC_OBJ",
    "ZEND_POST_DEC_OBJ",
    "ZEND_ECHO",
    "ZEND_OP_DATA",
    "ZEND_INSTANCEOF",
    "ZEND_GENERATOR_CREATE",
    "ZEND_MAKE_REF",
    "ZEND_DECLARE_FUNCTION",
    "ZEND_DECLARE_LAMBDA_FUNCTION",
    "ZEND_DECLARE_CONST",
    "ZEND_DECLARE_CLASS",
    "ZEND_DECLARE_CLASS_DELAYED",
    "ZEND_DECLARE_ANON_CLASS",
    "ZEND_ADD_ARRAY_UNPACK",
    "ZEND_ISSET_ISEMPTY_PROP_OBJ",
    "ZEND_HANDLE_EXCEPTION",
    "ZEND_USER_OPCODE",
    "ZEND_ASSERT_CHECK",
    "ZEND_JMP_SET",
    "ZEND_UNSET_CV",
    "ZEND_ISSET_ISEMPTY_CV",
    "ZEND_FETCH_LIST_W",
    "ZEND_SEPARATE",
    "ZEND_FETCH_CLASS_NAME",
    "ZEND_CALL_TRAMPOLINE",
    "ZEND_DISCARD_EXCEPTION",
    "ZEND_YIELD",
    "ZEND_GENERATOR_RETURN",
    "ZEND_FAST_CALL",
    "ZEND_FAST_RET",
    "ZEND_RECV_VARIADIC",
    "ZEND_SEND_UNPACK",
    "ZEND_YIELD_FROM",
    "ZEND_COPY_TMP",
    "ZEND_BIND_GLOBAL",
    "ZEND_COALESCE",
    "ZEND_SPACESHIP",
    "ZEND_FUNC_NUM_ARGS",
    "ZEND_FUNC_GET_ARGS",
    "ZEND_FETCH_STATIC_PROP_R",
    "ZEND_FETCH_STATIC_PROP_W",
    "ZEND_FETCH_STATIC_PROP_RW",
    "ZEND_FETCH_STATIC_PROP_IS",
    "ZEND_FETCH_STATIC_PROP_FUNC_ARG",
    "ZEND_FETCH_STATIC_PROP_UNSET",
    "ZEND_UNSET_STATIC_PROP",
    "ZEND_ISSET_ISEMPTY_STATIC_PROP",
    "ZEND_FETCH_CLASS_CONSTANT",
    "ZEND_BIND_LEXICAL",
    "ZEND_BIND_STATIC",
    "ZEND_FETCH_THIS",
    "ZEND_SEND_FUNC_ARG",
    "ZEND_ISSET_ISEMPTY_THIS",
    "ZEND_SWITCH_LONG",
    "ZEND_SWITCH_STRING",
    "ZEND_IN_ARRAY",
    "ZEND_COUNT",
    "ZEND_GET_CLASS",
    "ZEND_GET_CALLED_CLASS",
    "ZEND_GET_TYPE",
    "ZEND_ARRAY_KEY_EXISTS"
]

def match_opcode(handler_func_name):
    matched_op = ""
    for op in OPCODES:
        if handler_func_name.startswith(op):
            if len(op) > len(matched_op):
                matched_op = op

    if not matched_op:
        raise Exception("Can not find corresponding OPCODE for handler {0}".format(handler_func_name))

    return matched_op


if __name__ == '__main__':
    if len(sys.argv) == 1:
        filepath = sys.argv[0]
    else:
        filepath = "php7.0-fpm.log"

    prev_op = ""
    counter = {}
    cnt = 1

    with open(filepath) as fp:
        line = fp.readline()
        while line:
            handler_func_name = line[line.rfind(":")+1:-4]
            opcode = match_opcode(handler_func_name)
            # print("{}".format(opcode))
            if prev_op:
                pair_name = "{0}+{1}".format(prev_op, opcode)
                if pair_name in counter:
                    counter[pair_name] += 1
                else:
                    counter[pair_name] = 1

            prev_op = opcode

            line = fp.readline()
            cnt += 1

    print("total opcodes: {}".format(cnt))
    print("\nOpcode pair:")
    print(json.dumps(dict(sorted(counter.items(), key=lambda item: item[1], reverse=True)), indent=4))
