INSERT INTO ablt_eval_ques (eval_sheet_no,
                            ablt_ques_no,
                            eval_trgt_clss,
                            required_yn,
                            otpt_order,
                            ans_nmbr,
                            reg_mem_no,
                            modf_mem_no,
                            reg_dt,
                            modf_dt,
                            del_yn)
VALUES ('{{eval_sheet_no}}',
        '{{ablt_ques_no}}',
        '{{eval_trgt_clss}}',
        'Y',
        '{{otpt_order}}',
        null,
        '{{reg_mem_no}}',
        '{{modf_mem_no}}',
        sysdate(),
        sysdate(),
        'N')
ON DUPLICATE KEY UPDATE
    del_yn= 'N'
