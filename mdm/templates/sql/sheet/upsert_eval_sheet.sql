INSERT INTO eval_sheet (eval_sheet_no,
                            eval_clss,
                            sheet_nm,
                            sheet_desc,
                            reg_mem_no,
                            modf_mem_no,
                            reg_dt,
                            modf_dt,
                            del_yn)
VALUES ('{{eval_sheet_no}}',
        '{{eval_clss}}',
        '{{sheet_nm}}',
        '{{sheet_desc}}',
        '{{reg_mem_no}}',
        '{{modf_mem_no}}',
        sysdate(),
        sysdate(),
        'N')
ON DUPLICATE KEY UPDATE del_yn= 'N',
    sheet_desc = '{{sheet_desc}}',
    sheet_nm = '{{sheet_nm}}',
    modf_mem_no = '{{modf_mem_no}}',
    eval_clss = '{{eval_clss}}'